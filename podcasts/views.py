from email import contentmanager
from multiprocessing import context
from pyexpat import model
from sys import implementation
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Episode

# Create your views here.


class HomePageView(ListView):
    template_name = "podcasts/home.html"
    model = Episode

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by(
            "-pub_date")[:10]
        return context
