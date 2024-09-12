from django.urls import path
from .views import SnackDetailView, SnackListView


urlpatterns=[
    path('',SnackListView.as_view(), name='snack_list'),
    path('snack_detail/<int:pk>/', SnackDetailView.as_view(), name='snack_detail')
]
