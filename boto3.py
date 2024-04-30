
import os
import boto3

key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_DEFAULT_REGION")
endpoint = os.getenv("AWS_S3_ENDPOINT")
bucket_name = os.getenv("AWS_S3_BUCKET")

region

s3 = boto3.client(
    "s3",
    region,
    aws_access_key_id=key_id,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint,
    use_ssl=True
)

s3

response = s3.list_buckets()
response["Buckets"]

filename = "hello.txt"

s3.upload_file(filename, bucket_name, Key=filename)

objects = s3.list_objects_v2(Bucket=bucket_name)

for obj in objects["Contents"]:
    print(obj["Key"])

s3.download_file(bucket_name, filename, "downloaded_hello.txt") 


