from django.shortcuts import render,redirect
from .models import Products,Games
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def home(request):
	return render(request,'gamazon/home.html')

def about(request):
	return render(request,'gamazon/about.html')

def games(request):
	if request.method=="POST":
		gname=request.POST['gid']
		gid=Products.objects.filter(id=gname).first()
		if not Games.objects.filter(gid=gid,uid=request.user).exists():
			obj=Games.objects.create(gid=gid,uid=request.user)
			obj.save()
	dic={'game':Products.objects.all()}
	return render(request,'gamazon/games.html',dic)

@login_required	
def cart(request):
	if request.method=="POST":
		gname=request.POST['gid']
		gid=Products.objects.filter(id=gname).first()
		Games.objects.filter(gid=gid,uid=request.user).delete()
		
	games=Games.objects.filter(uid=request.user)
	games=[i.gid for i in games]
	return render(request,'gamazon/cart.html',{'game':games})

