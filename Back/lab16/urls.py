from django.contrib import admin
from django.urls import path, include
from .views import RegUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegUser, name='Register'),
    path('', include('Kitchen.urls'), name='Auth')
]
