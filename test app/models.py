from functools import total_ordering
from django.db import models
from django.db.models.deletion import get_candidate_relations_to_delete

class Users(models.Model):
    user_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=80)

class Genres(models.Model):
    genre_id=models.IntegerField(primary_key=True)
    genre_name=models.CharField(max_length=50)

class Movies(models.Model):
    movie_id=models.IntegerField(primary_key=True)
    movie_name=models.CharField(max_length=50)
    year=models.DateField()
    rating=models.FloatField()
    price=models.FloatField()
    genre_id=models.ForeignKey(Genres,on_delete=models.CASCADE)

class Movies_saved(models.Model):
    saved_movie_id=models.IntegerField(primary_key=True)
    movie_id=models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)

class Movies_viewed(models.Model):
    viewed_movie_id=models.IntegerField(primary_key=True)
    movie_id=models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_id=models.ForeignKey(Users, on_delete=models.CASCADE)

# u1=Users.objects.create(username="Kamila",email="user1@gmail.com",password="123456")
# u2=Users.objects.create(username="Tuba",email="user2@gmail.com",password="789456")
# u3=Users.objects.create(user_id=3,username="Yasmin",email="user3@gmail.com",password="541236")

# g1=Genres.objects.create(genre_id=1,genre_name="action")
# g2=Genres.objects.create(genre_id=2,genre_name="comedy")
# g3=Genres.objects.create(genre_id=3,genre_name="drama")
# g4=Genres.objects.create(genre_id=4,genre_name="war")
# g5=Genres.objects.create(genre_id=5,genre_name="fantasy")
# g6=Genres.objects.create(genre_id=6,genre_name="horror")
# g7=Genres.objects.create(genre_id=7,genre_name="family")
# g8=Genres.objects.create(genre_id=8,genre_name="adventure")

# m1=Movies.objects.create(movie_id=1,movie_name="No way home",year="2021-12-14",rating=5,price=3500.0,genre_id_id=1)
# m2=Movies.objects.create(movie_id=2,movie_name="Tom and Jerry",year="1940-05-05",rating=4.5,price=2500.0,genre_id_id=7)
# m3=Movies.objects.create(movie_id=3,movie_name="Space Sweepers",year="2021-12-31",rating=4.8,price=2000.0,genre_id_id=5)
# m4=Movies.objects.create(movie_id=4,movie_name="Fury",year="2014-04-21",rating=4.5,price=1500.0,genre_id_id=4)
# m5=Movies.objects.create(movie_id=5,movie_name="Good doctor",year="2021-07-18",rating=3.9,price=1600.0,genre_id_id=3)

# ms1=Movies_saved.objects.create(saved_movie_id=1,movie_id_id=1,user_id_id=1)
# ms2=Movies_saved.objects.create(saved_movie_id=2,movie_id_id=2,user_id_id=2)

# mv1=Movies_viewed.objects.create(viewed_movie_id=1,movie_id_id=3,user_id_id=1)
# mv2=Movies_viewed.objects.create(viewed_movie_id=2,movie_id_id=5,user_id_id=3)

