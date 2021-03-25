from django.test import TestCase
from .views import index, games, reviews
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import Genre, Game, Review
import datetime
from .forms import GenreForm, GameForm, ReviewForm

# Create your tests here.

# ==============================
# MODEL STRING & TABLENAME TEST
# ==============================

class GenreTest(TestCase):
    def setUp(self):
        self.genre = Genre(GenreName = 'Test Genre')

    def test_genrestring(self):
        self.assertEqual(str(self.genre), 'Test Genre')

    def test_tablename(self):
        self.assertEqual(str(Genre._meta.db_table), 'genre')



class GameTest(TestCase):
    def setUp(self):
        self.game = Game(GameTitle = 'Test Game')

    def test_gamestring(self):
        self.assertEqual(str(self.game), 'Test Game')

    def test_tablename(self):
        self.assertEqual(str(Game._meta.db_table), 'game')



class ReviewTest(TestCase):
    def setUp(self):
        self.review = Review(ReviewTitle = 'Test Review')

    def test_reviewstring(self):
        self.assertEqual(str(self.review), 'Test Review')

    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')


# ==============================
# VIEW TEST
# ==============================

class IndexViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class GamesViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)


class ReviewsViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)

# class GameDetailsViewTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='testuser')
#         self.genre = Genre.objects.create(GenreName='Test')
#         self.game = Game(GameTitle = "Title", Developer = 'Dev', Genre = self.genre, ReleaseDate = '0000-00-00', AverageHours = 5, GameUrl = 'http://www.url.com/', Description = 'Game', User = self.user)

#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('gamedetails', args=(self.game.id,)))
#         self.assertEqual(response.status_code, 200)


# ==============================
# FORM TEST
# ==============================

class TestGameForm(TestCase):
    def test_gameform(self):
        form=GameForm(data={
            'GameTitle':'Test Game', 
            'Developer':'Test Dev',
            'Genre':'Test Genre',
            'ReleaseDate':'2021-03-25',
            'AverageHours':'0',
            'GameUrl':'http://www.url.com/',
            'Description':'Game',
            'User':'admin'
        })
        self.assertTrue(form.is_valid)