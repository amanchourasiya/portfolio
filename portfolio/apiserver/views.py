from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apiserver.idgenerator import getID

@csrf_exempt
def image(request):
    if request.method=="POST":
        
        img_data=request.FILES['image'].read()
        ID=getID()

        fileobj=open("static/blog-images/"+str(ID)+".jpg","wb")
        fileobj.write(img_data)
        fileobj.close()
       
        data={"success" : 1,"file": {"url" : "http://amanchourasiya.com/static/blog-images/"+str(ID)+".jpg",}}
        

        return JsonResponse(data,safe=False)

