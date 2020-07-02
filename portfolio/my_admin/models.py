from django.db import models

class Login(models.Model):
    userName=models.CharField(max_length=100)
    passWord=models.CharField(max_length=100)
