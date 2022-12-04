from django.urls import path
from . import views

app_name = 'news'

#an index referring to our view
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

#need path for each question