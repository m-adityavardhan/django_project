from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
	name=models.CharField(max_length=100)
	price=models.IntegerField()
	pic=models.ImageField(upload_to="pics")

class Games(models.Model):
	gid=models.ForeignKey(Products,on_delete=models.CASCADE)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)
