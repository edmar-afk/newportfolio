
from django.urls import path
from . import views


urlpatterns = [
    path('homepage', views.main, name="homepage"),
    path('skills', views.skills, name="skills"),
    path('about', views.about, name="about"),
    path('works', views.works, name="works"),
    path('comments', views.comments, name="comments"),
    
    
     #couters for my emojis
    path('counter/', views.counter, name='counter'),
    path('counterheart/', views.counterheart, name='counterheart'),
    path('counterhaha/', views.counterhaha, name='counterhaha'),
    path('counterwow/', views.counterwow, name='counterwow'),
    path('countersad/', views.countersad, name='countersad'),
    path('counterangry/', views.counterangry, name='counterangry'),
]
