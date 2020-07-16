from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='game-home'),
    path('about/', views.about,name='game-about'),
    path('games/', views.games,name='game-games'),
    path('cart/', views.cart,name='game-cart')

]