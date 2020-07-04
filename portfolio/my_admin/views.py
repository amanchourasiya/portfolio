from django.shortcuts import render,redirect
from my_admin.models import Login
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import re
import os
from my_admin.html_generator import create_html
from my_admin.save_cards import save_cards

def login(request):
    return render(request, 'my_admin.html', {})

def check(request):
    print("before fun")
    if request.method=="POST":
        username=request.POST.get('username')  # Both variable name should be different
        password=request.POST.get('password')
        

        userName=os.environ['USERNAME']
        passWord=os.environ['PASSWORD']
        
        #print('post ' + username + ' ' + password)
        #print('env ' + userName + ' ' + passWord)
        if ((username == userName) and (password==passWord)):
            #print('Saving session')
            request.session['username']=username
            #print('Saved session')
            return redirect('./add_blog')
        else:
            username=None
            return render(request,'my_admin.html',{})

def add_blog(request):
    
   
    if request.session.has_key('username'):
        return render(request,'add_blog.html',{})
        
    else:
        return redirect('/')

def logout(request):
    del request.session['username']
    return redirect('/my_admin')

@csrf_exempt
def save_blog(request):
    if request.method=="POST":
        
        editor_data=json.loads(request.body)
        title=editor_data['blocks'][0]['data']['text']
        title=re.sub(r"\s+",'_',title)
        
        fileobj=open("blog/templates/blog/"+title+".html","w")
        fileobj.close()
        blog_card_data={title:editor_data}
       
        print(editor_data)
        save_cards(title,editor_data['blocks'])
        create_html(title,editor_data['blocks'])
        print("Html created successfully")
        link=title
        return JsonResponse(link,safe=False)
   
