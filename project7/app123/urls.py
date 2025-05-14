from django.contrib import admin
from django.urls import path
from app123.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('vicecaptain/',vicecaptain,name='vicecaptain'),
]