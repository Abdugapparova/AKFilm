from django import forms
from django.db import models
from django.forms import fields
from .models import Users, Movies,Genres,Movies_saved,Movies_viewed

class User(forms.ModelForm):
    class Meta:
        model=Users
        fields=[
            "user_id",
            "username",
            "email",
            "password",
        ]
class Genre(forms.ModelForm):
    class Meta:
        model=Genres
        fields=[
            "genre_id",
            "genre_name",
        ]

class Movie(forms.ModelForm):
    class Meta:
        model=Movies
        fields=[
            "movie_id",
            "movie_name",
            "year",
            "rating",
            "price",
            "genre_id",
        ]

class Saved_movie(forms.ModelForm):
    class Meta:
        model=Movies_saved
        fields=[
            "saved_movie_id",
            "movie_id",
            "user_id",
        ]

class Viewed_movie(forms.ModelForm):
    class Meta:
        model=Movies_viewed
        fields=[
            "viewed_movie_id",
            "movie_id",
            "user_id",
        ]