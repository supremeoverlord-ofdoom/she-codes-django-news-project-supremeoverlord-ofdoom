from django.views import generic
from .models import NewsStory

#class based views
class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()  #get news stroies and use them in index view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4] #get all the news stories, but only take the first 4
        context['all_stories'] = NewsStory.objects.all() #get all the stories
        return context  
    

