from django.db import models
from django.contrib.auth.models import User

class UserPhoto2(models.Model): 
    uid = models.CharField(max_length=50) 
    user_Img = models.ImageField(upload_to='images/') 

class FeaturePost(models.Model):
	uid = models.CharField(max_length=50) 
	title = models.CharField(max_length=50)
	user_Img = models.ImageField(upload_to='images/')
	created = models.DateTimeField(auto_now_add=True)
