from django.urls import path
from apiserver import views

urlpatterns = [
    path('image', views.image, name='image'),
    path('getviews/<slug:blog_name>/', views.get_views_and_claps, name='get_views_and_claps'),
    path('incrementviews', views.increment_views, name='increment_views'),
    path('incrementclaps', views.increment_claps, name='increment_claps'),
   
]
