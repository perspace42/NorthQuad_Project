'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Defines the urls for the entire website
'''

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("saga/", include("saga.urls")),
    path('admin/', admin.site.urls),
]
