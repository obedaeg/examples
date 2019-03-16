# S3 Examples

Here you can find examples of how to deal with s3 data, download a list of files, transform data, insert into db, etc.


## Boto3

For this examples we use boto3 library, which is the default library for python for every aws product, you can find documentation about boto3 [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html).

To install boto3 into your python project use the following command

```
pip install boto3
```

This automatically download and install the library into your environment.

## AWS Access

To use the library you need to have your aws access key and secret key, it is recommeded that you use aws cli in your computer to manager you credentials, you can check the installation guide [here](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-install.html) and then configure the cli by following [this](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-configure.html). Remember **don't use credentials in your code**.

## Postgresql

This tutorials use Postgres database, you can install the client for python with this command:

```
pip install psycopg2
```

And for better use you can check the documentation [here](http://initd.org/psycopg/docs/).
