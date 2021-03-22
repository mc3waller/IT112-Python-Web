from django.shortcuts import render, get_object_or_404
from .models import Game, Genre, Review

# Create your views here.

def index(request):
    return render(request, 'final/index.html')

def games(request):
    game_list = Game.objects.all()
    return render(request, 'final/games.html', {'game_list': game_list})

def gameDetails(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'final/gamedetails.html', {'game': game})

def reviews(request):
    review_list = Review.objects.all()
    return render(request, 'final/reviews.html', {'review_list': review_list})

def reviewDetails(request, id):
    review = get_object_or_404(Review, pk=id)
    return render(request, 'final/reviewdetails.html', {'review': review})