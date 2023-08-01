from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', login_request,name='login_request'),
    path('start/',start_button,name='start_button')
]