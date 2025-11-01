import json
import boto3
import os
import uuid

def lambda_handler(event, context):
    try:

        # Create an S3 client
        s3 = boto3.client('s3')

        # Call S3 to list current buckets
        objlist = s3.list_objects(
                        Bucket='bucketname',
                        MaxKeys = 10)

        print (objlist['Contents'])
        return str(objlist['Contents'])


    except Exception as e:
        print(e)
        raise e