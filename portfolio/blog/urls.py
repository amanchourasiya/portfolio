from django.urls import path
from blog import views

urlpatterns = [

    path('<slug:title>/', views.save_blog),
    path('tmp/<slug:title>', views.preview),
    path('', views.blog, name="blog"),

]
