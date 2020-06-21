import os.path
import json
def save_cards(title,editorjs):
    if os.path.isfile('static/blog-cards.json'):
        print("inside if")
        with open("static/blog-cards.json","r") as fileobj:
            previous_dict=json.load(fileobj)
        
        
        blog_card_data={title:editorjs}
    
        blog_card_data.update(previous_dict)
        
        fileobj=open("static/blog-cards.json","w")
        json.dump(blog_card_data,fileobj,indent=4)
        fileobj.close()
    else:
        blog_card_data={title:editorjs}
        with open("static/blog-cards.json","w") as fileobj:
            json.dump(blog_card_data,fileobj,indent=4)
    
