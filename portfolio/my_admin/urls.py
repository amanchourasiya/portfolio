from django.urls import path
from my_admin import views

urlpatterns = [
    path('', views.login, name='login'),
    path('check', views.check, name='check'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('logout/', views.logout, name='logout'),
    path('add_blog/blog_req/', views.save_blog, name='blog_req'),
    path('add_blog/preview_req/', views.preview_blog, name='preview_req'),
]
