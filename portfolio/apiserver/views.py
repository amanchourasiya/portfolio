from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .idgenerator import getID
from utils import boto3_util, imageutil
from apiserver.models import PostViews


@csrf_exempt
def image(request):
    print('In image upload')
    if request.method == "POST":

        img_data = request.FILES['image'].read()
        ID = getID()
        image_name = 'static/blog-images/' + ID
        with open(image_name, "wb") as f:
            f.write(img_data)
        try:
            new_image_name = imageutil.convert(image_name)
        except Exception as e:
            print(e)
        try:
            url = boto3_util.upload_image(new_image_name, str(ID) + '.png')
        except Exception as e:
            print(e)
        data = {'success': 1,
                'file':
                {'url': url}
                }
        return JsonResponse(data, safe=False)


def get_views_and_claps(request, blog_name):
    # Check if this is the first visit of post
    # If this is first view then add entry in DB and return default
    # Else return the post view count
    # Request should have Post/blog name , this will be used as key
    try:
        post = PostViews.objects.get(blog_id=blog_name)
    except PostViews.DoesNotExist:
        # Blog entry not present so this is first view of post
        post = PostViews(blog_id=blog_name, blog_view_count=0)
        post.save()
    data = {
        'blog_views': post.blog_view_count,
        'blog_claps': post.blog_claps
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def increment_views(request):
    if request.method == 'POST':
        blog_name = request.POST.get('blog_name')
        try:
            post = PostViews.objects.get(blog_id=blog_name)
            post.blog_view_count = post.blog_view_count + 1
        except PostViews.DoesNotExist:
            post = PostViews(blog_id=blog_name, blog_view_count=1)
        post.save()
        return JsonResponse({}, safe=False)

@csrf_exempt
def increment_claps(request):
    if request.method == 'POST':
        blog_name = request.POST.get('blog_name')
        try:
            post = PostViews.objects.get(blog_id=blog_name)
            post.blog_claps = post.blog_claps + 1
        except PostViews.DoesNotExist:
            post = PostViews(blog_id=blog_name, blog_claps=1)
        post.save()
        return JsonResponse({}, safe=False)   