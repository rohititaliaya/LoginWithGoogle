
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import*

class uploadForm(forms.ModelForm): 
  
    class Meta: 
        model = UserPhoto2
        fields = ['uid', 'user_Img'] 

class uploadPost(forms.ModelForm):

    class Meta:
        model = FeaturePost
        fields='__all__'