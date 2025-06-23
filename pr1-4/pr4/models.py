from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    rights = models.IntegerField()
    date_add = models.DateField()

class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    date_add = models.DateField()
    date_add_last = models.DateField()

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add = models.DateField()

class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    id_podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    media_link = models.CharField(max_length=256)
    date_add = models.DateField()
    durations = models.IntegerField()

class Podcast_genre(models.Model):
    id = models.AutoField(primary_key=True)
    id_podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    id_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class Episode_genre(models.Model):
    id = models.AutoField(primary_key=True)
    id_episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    id_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    id_episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField()

class Group_authors(models.Model):
    id = models.AutoField(primary_key=True)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    id_podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

class User_groups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Group_episodes(models.Model):
    id = models.AutoField(primary_key=True)
    id_group = models.ForeignKey(User_groups, on_delete=models.CASCADE)
    id_episode = models.ForeignKey(Episode, on_delete=models.CASCADE)