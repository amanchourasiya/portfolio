from django.shortcuts import render,redirect
from my_admin.models import Login
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import re
from my_admin.html_generator import create_html
from my_admin.save_cards import save_cards

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
   
