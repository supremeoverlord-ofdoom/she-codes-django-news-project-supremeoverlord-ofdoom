from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField() #if you want long text rather than in charfield
    news_image = models.URLField(blank=True) #ADDED IN:  a field to the NewsStory model for an image url 

#created the form but not the answers