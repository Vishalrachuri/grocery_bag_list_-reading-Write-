from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('/', views.home),
    path('login',views.login),
    path('register',views.register),
    path('search/<str:username>',views.search),
    path('add/<str:username>',views.add)
]