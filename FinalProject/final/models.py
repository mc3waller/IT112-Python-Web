from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# REMINDER: ID's are auto-generated outside of the code found here

class Genre(models.Model):
    GenreName = models.CharField(max_length=255)
    GenreDescription = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.GenreName
    
    class Meta:
        db_table = 'genre'

class Game(models.Model):
    GameTitle = models.CharField(max_length=255)
    Developer = models.CharField(max_length=255)
    Genre = models.ForeignKey(Genre, on_delete = models.DO_NOTHING)
    ReleaseDate = models.DateField()
    AverageHours = models.IntegerField()
    GameUrl = models.URLField()
    Description = models.TextField()
    User = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.GameTitle

    class Meta:
        db_table = 'game'

class Review(models.Model):
    ReviewTitle = models.CharField(max_length=255)
    GameTitle = models.ForeignKey(Game, on_delete = models.CASCADE)
    ReviewDate = models.DateField()
    ReviewContent = models.TextField()
    User = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.ReviewTitle

    class Meta:
        db_table = 'review'