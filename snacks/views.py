from django.shortcuts import render
from django.urls import path
from django.db import models
from .models import Snack
from django.views.generic import ListView, DetailView
# from django.views.generic.detail import DetailView

# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack    