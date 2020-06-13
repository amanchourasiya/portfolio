from django.shortcuts import render,redirect
from my_admin.models import Login
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import re
from my_admin.html_generator import create_html


def login(request):
    return render(request, 'my_admin.html', {})

def check(request):
    print("before fun")
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        userName=Login.objects.values('userName')
        passWord=Login.objects.values('passWord')
        

        if ((username == userName[0]['userName']) and (password==passWord[0]['passWord'])):
            request.session['username']=username
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
def blog(request):
    if request.method=="POST":
        
        editor_data=json.loads(request.body)
        title=editor_data['blocks'][0]['data']['text']
        title=re.sub(r"\s+",'_',title)
        print("title:",title)
        fileobj=open("my_admin/templates/blog/"+title+".html","w")
        fileobj.close()
        create_html(title,editor_data['blocks'])
        print("Html created successfully")
        
        return render(request,'my_admin.html')
   
