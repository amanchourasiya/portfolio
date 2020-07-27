#!/usr/bin/env python3

'''
This script will setup the server environment including getting files from persistent storage
and start server after running some pre checks.

This will setup config based on development/production environment
'''

import sys
import os
import json
import boto3

sys.path.append(os.getcwd() + '/portfolio/my_admin')
from html_generator import create_html


def usage():
    print('Script usage')
    print('python3 start_server.py <server-mode>')
    print('server-mode: dev/prod')


def dev_mode():
    # Check prerequisites
    check_prerequisites()
    generate_blogs()
    # Start server
    start()


def prod_mode():
    # Cleanup dev blogs used for testing
    cleanup_dev_data()

    # Check prerequisites
    check_prerequisites()

    # Download images and blog JSON from persistent storage
    get_persistent_data()

    # Start server
    start()


def start():
    port = os.environ.get('PORT', 80)
    os.system('gunicorn -b 0.0.0.0:' + str(port) +
              ' --chdir portfolio/ portfolio.wsgi --log-file -')


def cleanup_dev_data():
    data_dir = 'portfolio/static'

    # Removing blog images
    cmd = f'rm -rf {data_dir}/blog-images/*'
    os.system(cmd)

    # Removing old blog-cards.json
    cmd = f'rm -rf {data_dir}/blog-cards.json'
    os.system(cmd)

    # Cleanup images marker file
    os.system('rm -f portfolio/static/.count.txt')

    # Cleanup blog html
    cmd = 'rm -rf portfolio/blog/templates/blog/*'
    os.system(cmd)


def get_persistent_data():
    try:
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
        aws_region = os.environ['AWS_REGION']
        bucket_name = os.environ['AWS_BUCKET_NAME']
    except:
        print('AWS credentials not supplied in env')
        sys.exit(1)

    blog_json_file = 'portfolio/static/blog-cards.json'

    s3 = boto3.resource('s3',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region)

    try:
        s3.meta.client.download_file(Bucket=bucket_name,
                                     Key='blogs/blog-cards.json',
                                     Filename=blog_json_file)
    except:
        pass

    # Download image counter
    try:
        s3.meta.client.download_file(Bucket=bucket_name,
                                     Key='count.txt',
                                     Filename='portfolio/static/.count.txt')
    except:
        reset_counter()

    # Download all blog images
    get_blog_images(s3, bucket_name)

    # Generate blogs html
    generate_blogs()


def get_blog_images(s3_resource, bucket_name):
    store_path = 'portfolio/static/blog-images/'
    bucket = s3_resource.Bucket(bucket_name)
    for s3_object in bucket.objects.filter(Prefix='blog-images/'):
        _, filename = os.path.split(s3_object.key)
        bucket.download_file(s3_object.key, store_path + '/' + filename)


def reset_counter():
    with open('portfolio/static/.count.txt', 'w') as f:
        f.write('0')


def generate_blogs():
    if not os.path.exists('portfolio/static/blog-cards.json'):
        return
    with open('portfolio/static/blog-cards.json', 'r') as f:
        blogs = json.load(f)
    path = 'portfolio/blog/templates/blog/'
    for blog in blogs:
        create_html(blog, blogs[blog], path=path)


def check_prerequisites():
    # Check for necessary directory
    required_dir = [
        'portfolio/static/blog-images',
        'portfolio/blog/templates/blog',
        'portfolio/blog/templates/blog/tmp'
    ]

    for dir in required_dir:
        if not os.path.exists(dir):
            cmd = f'mkdir -p {dir}'
            os.system(cmd)
            print(f'Creating {dir} dir')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        mode = sys.argv[1]
        if mode == 'dev':
            dev_mode()
        elif mode == 'prod':
            prod_mode()
        else:
            usage()
