import json
import os
from tempfile import NamedTemporaryFile

import boto3
import psycopg2

BUCKET_NAME = ''
S3_PATH=''

DB_NAME=''
DB_USER=''
DB_PASS=''
DB_HOST='localhost'
DB_PORT=5432

INSERT_COMMAND='INSERT INTO _table_name_(field_1, field_2, field_3) VALUES (%s, %s, %s)'

if __name__ == "__main__":
    s3 = boto3.client('s3')
    objects = s3.list_objects(Bucket=BUCKET_NAME,  Prefix=S3_PATH)

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cursor = conn.cursor()

    i = 0
    for obj in objects['Contents']:
        i = i + 1
        s3_file = obj['Key']
        print(f'Downloading file {i}: {s3_file}')
        tmp_file = NamedTemporaryFile(prefix=".json", delete=False).name

        s3.download_file(Bucket = BUCKET_NAME,Key=s3_file, Filename=tmp_file)
        with open(tmp_file, mode='r') as f:
            content = f.readline()
            if content:
                j = json.loads(content)
                field_1 = j.get("parent", {}).get("field_1")
                field_2 = j.get("parent", {}).get("another_parent", {}).get("field_2")
                field_list = j.get("parent", {}).get("another_parent", {}).get("field_list")
                for result in field_list or []:
                    field_3 = result["field_3"]
                    tuple = (field_1, field_2, field_3)
                    print(f'Inserting {tuple}')
                    cursor.execute(INSERT_COMMAND, tuple)
                    conn.commit()

        os.remove(tmp_file)



