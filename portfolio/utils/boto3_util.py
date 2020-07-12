import boto3
import sys
import os


image_url = 'https://amanchourasiya.s3.ap-south-1.amazonaws.com/'
bucket_name = 'amanchourasiya'
region = 'ap-south-1'
def get_s3():
    try:
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    except:
        print('AWS credentials not supplied in env')
        sys.exit(1)
    global region
    aws_region = region

    global __s3
    __s3 = boto3.resource('s3',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region )
    return __s3

def get_bucket_name():
    global __bucket_name
    if not __bucket_name:
        __bucket_name = 'amanchourasiya'
    
    return __bucket_name

def get_region():
    global __region
    if not __region:
        __region = 'ap-south-1'
    
    return __region

def upload_persistent_data(file_name, key):
    s3 = get_s3()                
    s3.meta.client.upload_file(Bucket=bucket_name,
                               Filename=file_name,
                               Key=key)

def upload_images(path, count):
    s3 = get_s3()
    for i in count:
        key = 'blog-images/image-' + str(i) + '.jpg'
        file_name = path + 'image-' + str(i) + '.jpg'

        s3.meta.client.upload_file(Bucket=get_bucket_name(),
                                   Filename=file_name,
                                   Key=key)

'''
    upload_image function will upload image to S3 bucket
    params:
      iamge_name: Name/path of image present on server
      image_key: Key to be used for storing image on S3
    return:
      It will return URL of the uploaded image to be used by other apps.
''' 
def upload_image(image_name, image_key):
    global image_url
    s3 = get_s3()
    key = 'blog-images/' + image_key
    print(image_name, key)
    s3.meta.client.upload_file(Bucket=bucket_name,
                               Filename=image_name,
                               Key=key)
    return image_url + 'blog-images/' + image_key