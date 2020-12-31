from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Index(request):
	x=ulogin()

	if request.method == 'POST':
		unm=request.POST.get('Username')
		pwd=request.POST.get('Password')

		user = authenticate(request,username=unm,password=pwd)

		if user is not None:
			login(request, user)
			messages.success(request, 'Login successfully for '+unm+' !!!')
			return redirect('Home',unm)
		else:
			messages.info(request,'Username and Password Incorrect !!!')

	xcontext={'user':x}
	return render(request,'login.html',xcontext)

def Register(request):	
	xuser=CreateUserForm()
	yuser=ProfileForm()
	
	if request.method == 'POST':
		xuser=CreateUserForm(request.POST)
		yuser=ProfileForm(request.POST)
		if xuser.is_valid() and yuser.is_valid():
			mx= xuser.save()
			userx = xuser.cleaned_data.get('username')
			yuser= yuser.save(commit=False)
			yuser.muser=mx
			yuser.save()
			messages.success(request, 'Account was created successfully for '+userx+' !!!')
			return redirect('login')

	xcontext={'user':xuser,'yuser':yuser}		
	return render(request,'Register.html',xcontext)

login_required(login_url='login')
def Home(request,pk):
	userdata= User.objects.get(username=pk)
	context={'userdata':userdata}
	return render(request,'Home.html',context)

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
			form.save()
			return redirect('upload')
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
