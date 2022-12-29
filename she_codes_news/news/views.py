from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth import get_user_model
# class based views


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()   #.order_by('-pub_date')  # get news stories and use them in index view ADDED IN: ordering news stories newest to oldest but i don't think its working

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all the news stories, but only take the first 4
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4] #ADDED IN: ordering news stories newest to oldest 
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')  #ADDED IN: ordering news stories newest to oldest 
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story' #overrrides 

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AuthorProfileView(generic.DetailView):
    model = get_user_model()
    template_name = 'news/profileDetail.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
    #     return context