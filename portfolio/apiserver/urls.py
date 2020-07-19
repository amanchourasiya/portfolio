from django.urls import path
from apiserver import views

urlpatterns = [
    path('image', views.image, name='image'),
    path('getviews/<slug:blog_name>/', views.get_views, name='getviews'),
    path('incrementviews', views.increment_views, name='increment_views'),
   
]
