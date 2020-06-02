from django.urls import path
from port import views

urlpatterns = [
    path('', views.port, name='port'),
]
