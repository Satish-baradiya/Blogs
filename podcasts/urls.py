import imp
from unicodedata import name
from django import views
from django.urls import path
from . views import HomePageView

urlpatterns = [ 
    path("", HomePageView.as_view(),name="home"),

]
