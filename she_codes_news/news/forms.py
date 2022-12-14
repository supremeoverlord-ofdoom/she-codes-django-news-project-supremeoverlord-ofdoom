from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'news_image',]
        labels = {
            'title': ('Article Title'),
            'pub_date': ('Publication Date'),
            'content': ('Article Content'),
            'news_image': ('URL of Article Image'),
        }
        help_texts = {
            'pub_date': ('(The date which the article is published)'),
            'news_image': (' (A URL from an image online that you wish to use for the article) '),
        }
        widgets = {
        'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
    }



