from django.shortcuts import render
import json
import os

def add_blog(request,title):
    
   return render(request,"blog/"+title+".html")


def blog(request):
    if not os.path.exists('static/blog-cards.json'):
        return render(request, 'blog.html',{})
    with open("static/blog-cards.json","r") as fileobj:
        data=json.load(fileobj)

    return render(request,"blog.html",{'data':data})
