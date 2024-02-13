from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
path ('',views.index),
path ('login',views.logins),
path ('register',views.register),
path ('adindex',views.adindex),
path ('userindex',views.userindex),
path ('complaint',views.complaint),
path ('feedback',views.feedback),
]