from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('games/', views.games, name = 'games'),
    path('gamedetails/<int:id>', views.gameDetails, name = 'gamedetails'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('reviewdetails/<int:id>', views.reviewDetails, name = 'reviewdetails'),
]