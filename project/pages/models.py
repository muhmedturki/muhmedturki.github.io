from django.db import models
from datetime import datetime

class JoinForm(models.Model):
    number= models.CharField(max_length=6, null=True, blank=True)
    name=models.CharField(max_length=100, null=True,blank=True)
    phone=models.CharField(max_length=50, null=True,blank=True)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    