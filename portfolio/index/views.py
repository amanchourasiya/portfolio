from django.shortcuts import render
import json
import os


def index(request):
    if os.path.exists('static/blog-cards.json'):
        with open("static/blog-cards.json", "r") as fileobj:
            data = json.load(fileobj)
        return render(request, 'index.html', {'data': data})
    else:
        return render(request, 'index.html', {'data': {}})
