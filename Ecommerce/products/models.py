from django.db import models

class Products(models.Model):
    name= models.CharField(max_length=40)
    price= models.FloatField()
    description= models.CharField(max_length=200, null=True, blank=True)
    is_active=models.BooleanField(default=True)
    creation_date=models.DateField(auto_now_add=True,null=True,blank=True)

class category(models.Model):
    name= models.CharField(max_length=50)