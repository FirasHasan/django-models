from django.shortcuts import render
from django.urls import path
from .views import SnackDetailView, SnackListView

# Create your views here.

urlpatterns=[
    path('',SnackListView.as_view(), name='snack_list'),
    path('snack_detail/<int:pk>/', SnackDetailView.as_view(), name='snack_detail')
]