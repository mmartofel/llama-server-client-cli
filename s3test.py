import boto3
import os

# Specify your AWS credentials
aws_s3_endpoint = 'http://127.0.0.1:9000'
aws_access_key_id = 'minio'
aws_secret_access_key = 'minio123'
aws_region = 'us-east-1'

# Create an S3 client
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region,
                  endpoint_url=aws_s3_endpoint)

def list_buckets():
    # List all buckets owned by the authenticated sender of the request
    response = s3.list_buckets()
    print("List of S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")

def upload_file(bucket_name, file_path):
    # Upload a file to a specific bucket
    file_name = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, bucket_name, file_name)
        print(f"{file_path} uploaded successfully to {bucket_name}")
    except Exception as e:
        print(f"Upload failed: {e}")

if __name__ == "__main__":
    # Example usage
    list_buckets()
    bucket_name = 'YOUR_BUCKET_NAME'
    file_path = 'path/to/your/file'
    upload_file(bucket_name, file_path)

