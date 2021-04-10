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
    path('profile/<slug:slug>/', views.profile, name='profile'),
    path('profile2/<int:id>/', views.profile2, name='profile2'),
    path('fundraise', views.fundraise, name='fundraise'),
       path('monthly_donation', views.monthly_donation, name='monthly_donation'),
    path('send_invitation/<slug:slug>/', views.send_invitation, name='send_invitation'),
    path('notification',views.notification,name='notification'),
    path('feedback_after_event/<int:id>/',views.feedback_after_event,name='feedback_after_event'),
    path('hosting_event/<slug:slug>/',views.hosting_event,name='hosting_event'),
   
]