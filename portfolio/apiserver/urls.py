from django.urls import path
from apiserver import views

urlpatterns = [
    path('', views.image, name='image'),

]
