from django.shortcuts import render, redirect
from my_admin.models import Login
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import re
import os
import glob
from my_admin.html_generator import create_html
from my_admin.save_cards import save_cards
import datetime


def login(request):
    return render(request, 'my_admin.html', {})


def check(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        userName = os.environ['USERNAME']
        passWord = os.environ['PASSWORD']
        if ((username == userName) and (password == passWord)):
            request.session['username'] = username
            return redirect('./add_blog')
        else:
            username = None
            return render(request, 'my_admin.html', {})


def add_blog(request):
    if request.session.has_key('username'):
        return render(request, 'add_blog.html', {})

    else:
        return redirect('/')


def logout(request):
    del request.session['username']
    return redirect('/my_admin')


@csrf_exempt
def save_blog(request):
    if request.method == "POST":
        editor_data = json.loads(request.body)
        title = editor_data['blocks'][0]['data']['text']
        title = process_title(title)

        process_date(editor_data)

        save_cards(title, editor_data['blocks'])
        create_html(title, editor_data['blocks'])
        link = title
        clear_tmp_blogs()
        return JsonResponse(link, safe=False)


@csrf_exempt
def preview_blog(request):
    editor_data = json.loads(request.body)
    title = editor_data['blocks'][0]['data']['text']
    title = process_title(title)

    process_date(editor_data)
    create_html(title, editor_data['blocks'], path='blog/templates/blog/tmp/')
    link = 'tmp/' + title
    return JsonResponse(link, safe=False)

# Utility methods


def process_title(title):
    title = title.lower()
    for c in title:
        if not c.isalnum():
            title = title.replace(c, '-')
    return title


def process_date(editor_data):
    date = datetime.date.today()
    date = date.strftime("%d %B %Y")
    editor_data['blocks'][0].update({'date': date})


def clear_tmp_blogs():
    files = glob.glob('blog/templates/blog/tmp/*')
    for f in files:
        os.remove(f)
