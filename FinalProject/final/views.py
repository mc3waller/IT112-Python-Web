from django.shortcuts import render, get_object_or_404
from .models import Game, Genre, Review
from . forms import GenreForm, GameForm, ReviewForm

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


def addGenre(request):
    form = GenreForm

    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = GenreForm()
    else:
        form = GenreForm()
    return render(request, 'final/addgenre.html', {'form': form})


def addGame(request):
    form = GameForm

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = GameForm()
    else:
        form = GameForm()
    return render(request, 'final/addgame.html', {'form': form})


def addReview(request):
    form = ReviewForm

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
    return render(request, 'final/addreview.html', {'form': form})