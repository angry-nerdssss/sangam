from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # this path is for main page
]