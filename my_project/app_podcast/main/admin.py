from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Podcast)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Episode)
admin.site.register(Podcast_genre)
admin.site.register(Episode_genre)
admin.site.register(Rating)
admin.site.register(Group_authors)
admin.site.register(User_groups)
admin.site.register(Group_episodes)