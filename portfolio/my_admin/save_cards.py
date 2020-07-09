import os.path
import json
from utils import boto3_util

def save_cards(title,editorjs):
    block_cards_file = 'static/blog-cards.json'

    if os.path.isfile(block_cards_file):
        with open(block_cards_file,"r") as fileobj:
            previous_dict=json.load(fileobj)
        
        blog_card_data={title:editorjs}
        blog_card_data.update(previous_dict)
        
        fileobj=open(block_cards_file,"w")
        json.dump(blog_card_data,fileobj,indent=4)
        fileobj.close()
    else:
        blog_card_data={title:editorjs}
        with open(block_cards_file,"w") as fileobj:
            json.dump(blog_card_data,fileobj,indent=4)

    # Saving persistent data 
    save_persistent_data()
    
    
def save_persistent_data():
    # Saving blog-cards.json to persistent storage , this file is used to generate 
    # data dynamically
    boto3_util.upload_persistent_data('static/blog-cards.json', 'blogs/blog-cards.json')
    with open('static/.count.txt', 'r') as f:
        count = int(f.read())
    
    with open('static/.prev_count.txt') as f:
        prev_count = int(f.read())
    
    files_tobe_uploaded = range(prev_count + 1, count + 1)
    boto3_util.upload_images('static/blog-images/', files_tobe_uploaded)

    # Uploading count marker file
    boto3_util.upload_persistent_data('static/.count.txt','count.txt')
