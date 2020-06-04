from django.urls import path
from my_admin import views

urlpatterns = [
    path('', views.login, name='login'),
    path('check', views.check, name='check'),
]
