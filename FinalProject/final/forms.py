from django import forms
from .models import Genre, Game, Review

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'