from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('register', views.registration, name='register'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('person', views.person, name='person')
]