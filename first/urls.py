from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # this path is for main page
        # to call the register page
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),  # to call the logout function
       path('feedback', views.feedback, name='feedback'),  # to call the logout function
    path('showfeedback', views.show_feedback, name='show_feedback'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),  # to call the login page
    # path('logout', views.logout, name='logout'),  # to call the logout function
]