from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	muser = models.OneToOneField(User, on_delete=models.CASCADE)
	Phonenumber = models.CharField(verbose_name="phone number",max_length=10)

class UserPhoto2(models.Model): 
    uid = models.CharField(max_length=50) 
    user_Img = models.ImageField(upload_to='images/') 

class FeaturePost(models.Model):
	uid = models.CharField(max_length=50) 
	title = models.CharField(max_length=50)
	user_Img = models.ImageField(upload_to='images/')
	created = models.DateTimeField(auto_now_add=True)
