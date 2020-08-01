from django.urls import path
from blog import views

urlpatterns = [

     path('<slug:title>/', views.add_blog),
     path('', views.blog,name="blog"),
     path('tmp/<slug:title>', views.preview),
]
