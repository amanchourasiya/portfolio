import boto3
import sys
import os

def upload_persistent_data(file_name, key):
    try:
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    except:
        print('AWS credentials not supplied in env')
        sys.exit(1)
        
    aws_region = 'ap-south-1'
    global bucket_name
    bucket_name = 'amanchourasiya'
    
    global s3
    s3 = boto3.resource('s3',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region )
                        
    s3.meta.client.upload_file(Bucket=bucket_name,
                               Filename=file_name,
                               Key=key)

def upload_images(path, count):
    global bucket_name
    global s3
    for i in count:
        key = 'blog-images/image-' + str(i) + '.jpg'
        file_name = path + 'image-' + str(i) + '.jpg'
        s3.meta.client.upload_file(Bucket=bucket_name,
                                   Filename=file_name,
                                   Key=key)

