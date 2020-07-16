from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


def register(request):
	if request.method=="POST":
		username=request.POST['username']
		pwd1=request.POST['psw']
		pwd2=request.POST['psw-repeat']
		if pwd1==pwd2:
			if User.objects.filter(username=username).exists():
				return render(request,'users/register.html',{'uname':'Username Already Taken'})
			else:
				user=User.objects.create_user(username=username,password=pwd1)
				user.save()
				messages.success(request,'Your account is created! Please login')
				return redirect('user-login')
		else:
			return render(request,'users/register.html',{'pass':'Passwords Didnot Match'})
	else:
		return render(request,'users/register.html')
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		pwd=request.POST['psw']

		user=auth.authenticate(username=username,password=pwd)

		if user:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'invalid credentials')
			return render(request,'users/login.html')
	else:
		return render(request,'users/login.html')
def logout(request):
	auth.logout(request)
	return redirect('/')