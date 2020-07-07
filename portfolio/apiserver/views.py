from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from idgenerator import getID

@csrf_exempt
def image(request):
    print('In image upload')
    if request.method=="POST":
        
        img_data=request.FILES['image'].read()
        ID=getID()
        print(id,ID)
        fileobj=open("static/blog-images/"+str(ID)+".jpg","wb")
        fileobj.write(img_data)
        fileobj.close()
       
        data={"success" : 1,"file": {"url" : "/static/blog-images/"+str(ID)+".jpg",}}
        

        return JsonResponse(data,safe=False)

