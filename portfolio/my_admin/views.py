from django.shortcuts import render,redirect
from my_admin.models import Login
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
def image(request):
    if request.method=="POST":
        
        img_data=request.FILES['image'].read()

        fileobj=open("static/blog-images/blog-image1.jpg","wb")
        fileobj.write(img_data)
        fileobj.close()
       
        data={"success" : 1,"file": {"url" : "http://127.0.0.1:8000/static/blog-images/blog-image1.jpg",}}
        

        return JsonResponse(data,safe=False)


    
