from django.shortcuts import render
from my_admin.models import Login

def login(request):
    return render(request, 'my_admin.html', {})

def check(request):
    print("before fun")
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)

        userName=Login.objects.values('userName')
        passWord=Login.objects.values('passWord')
        

        if ((username == userName[0]['userName']) and (password==passWord[0]['passWord'])):
            return render(request,'blog.html',{})
        else:
            return render(request,'my_admin.html',{})
