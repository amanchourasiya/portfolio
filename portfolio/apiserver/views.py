from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .idgenerator import getID
from utils import boto3_util


@csrf_exempt
def image(request):
    print('In image upload')
    if request.method == "POST":

        img_data = request.FILES['image'].read()
        ID = getID()
        image_name = 'static/blog-images/' + ID + '.jpg'
        with open(image_name, "wb") as f:
            f.write(img_data)
        print(image_name)
        try:
            url = boto3_util.upload_image(image_name, str(ID) + '.jpg')
        except Exception as e:
            print(e)
        data = {'success': 1,
                'file':
                {'url': url}
                }
        print('url:', url)

        return JsonResponse(data, safe=False)
