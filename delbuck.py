import boto3
import botocore
import json

s3_client = boto3.client(
    "s3",
    aws_access_key_id="AKIAJPT3CC56IEI4ZN3Q",
    aws_secret_access_key="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"
)

response = s3_client.list_buckets()
for bucket in response["Buckets"]:
    # Only removes the buckets with the name you want.
    if "bucket-to-remove" in bucket["Name"]:
        s3_objects = s3_client.list_objects_v2(Bucket=bucket["Name"])
        # Deletes the objects in the bucket before deleting the bucket.
        if "Contents" in s3_objects:
            for s3_obj in s3_objects["Contents"]:
                rm_obj = s3_client.delete_object(
                    Bucket=bucket["Name"], Key=s3_obj["Key"])
                print(rm_obj)
        rm_bucket = s3_client.delete_bucket(Bucket=bucket["Name"])
        print(rm_bucket)
