from django.shortcuts import render
from .models import Game, Genre, Review

# Create your views here.

def index(request):
    return render(request, 'final/index.html')

def games(request):
    game_list = Game.objects.all()
    return render(request, 'final/games.html', {'game_list': game_list})