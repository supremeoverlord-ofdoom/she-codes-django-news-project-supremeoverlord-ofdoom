from django.urls import path
from . import views

app_name = 'news'

# an index referring to our view
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>', views.AuthorProfileView.as_view(), name="profileDetail"),
]

# need path for each question
