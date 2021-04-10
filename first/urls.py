from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # this path is for main page
        # to call the register page
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),  # to call the logout function
]