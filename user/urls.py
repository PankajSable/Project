from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from user import views

urlpatterns = [
     path('', views.index, name="Home"),
     path('user', views.user, name="User"),
     path('post', views.Post, name="Post"),
     

]
