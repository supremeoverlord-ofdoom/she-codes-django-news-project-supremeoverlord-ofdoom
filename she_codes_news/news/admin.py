from django.contrib import admin

# import your models here
from .models import NewsStory #importing stories

# Register your models here.
admin.site.register(NewsStory)