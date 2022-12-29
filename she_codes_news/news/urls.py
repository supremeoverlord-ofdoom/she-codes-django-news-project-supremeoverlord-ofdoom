from django.urls import path
from . import views

app_name = 'news'

# an index referring to our view
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('author/<int:pk>/', views.AuthorProfileView.as_view(), name="profileDetail"), #pk is saying I expect and id here
]

# need path for each question
