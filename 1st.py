import boto3
from boto3.s3.transfer import S3Transfer

client = boto3.client(
    's3',
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key'
)

transfer = S3Transfer(client)
transfer.upload_file(
    'local path',
    'bucket_name',
    's3 directory with file name'
)
