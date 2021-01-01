from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Index(request):
	return render(request,'login.html')

def logout(request):
	# logout(request)
	return redirect('login')

def google(request):
	x = request.user
	return render(request,'google.html',{'usx':x})

def upload(request,pk):
	x=pk
	y=UserPhoto2.objects.filter(uid=x)
	if request.method == 'POST':
		form=uploadForm(request.POST,request.FILES)
		if form.is_valid():
			userid = request.POST.get('uid')
			form.save()
			return redirect('google')
	else:
		form = uploadForm()
	return render(request,'upload.html',{'form':form,'up':y})

def feature(request,pk):
	y=uploadPost()
	if request.method == 'POST':
		form=uploadPost(request.POST,request.FILES)
		if form.is_valid():
			userid = request.POST.get('uid')
			form.save()
			return redirect('seepost'+'/'+userid)
	else:
		y=uploadPost()
	return render(request,'feature.html',{'form':y})

def seepost(request,pk):
	x = pk
	y=FeaturePost.objects.filter(uid=x)
	return render(request,'seepost.html',{'usx':y})
