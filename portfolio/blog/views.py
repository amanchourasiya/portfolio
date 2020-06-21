from django.shortcuts import render
import json


def add_blog(request,title):
    
   return render(request,"blog/"+title+".html")


def blog(request):
    with open("static/blog-cards.json","r") as fileobj:
        data=json.load(fileobj)
    print(data)
        

    return render(request,"blog.html",{'data':data})
