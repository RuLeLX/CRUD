from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', AuthUser, name='Auth'),
    path('create_cooker/', CreateCooker, name='CreateCooker')
]