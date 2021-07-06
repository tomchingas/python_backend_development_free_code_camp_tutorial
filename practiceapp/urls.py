from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') #returns index function from views.py in app folder
]