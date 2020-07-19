from django.shortcuts import render
import json
import os

def add_blog(request,title):
    return render(request,"blog/"+title+".html")

def save_blog(request, title):
    return render(request, "blog/" + title + ".html")


def preview(request, title):
    return render(request, 'blog/tmp/' + title + '.html')


def blog(request):
    if not os.path.exists('static/blog-cards.json'):
        return render(request, 'blog.html', {})
    with open("static/blog-cards.json", "r") as fileobj:
        data = json.load(fileobj)

<<<<<<< HEAD
    return render(request,"blog.html",{'data':data})
=======
    return render(request, "blog.html", {'data': data})
>>>>>>> 6291810b206c150ab06e937bdd9cb07c9075d393
