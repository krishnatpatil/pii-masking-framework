import boto3
from .connector import DatabaseConnector

class S3Connector(DatabaseConnector):
    def __init__(self, access_key, secret_key, bucket, region):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        self.bucket = bucket

    def get_engine(self):
        # S3 does not use an engine like SQL databases
        return self.s3_client

    def get_metadata(self):
        response = self.s3_client.list_objects_v2(Bucket=self.bucket)
        metadata = [obj['Key'] for obj in response.get('Contents', [])]
        return metadata
