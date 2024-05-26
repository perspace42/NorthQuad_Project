'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Defines the urls for the saga application
'''

from django.urls import path
from . import views

app_name = "saga"

urlpatterns = [
    #ex: /saga/
    path("", views.index, name = "index"),
    #ex: /saga/results/Anglo_Saxons
    path("results/<str:factionId>",views.results, name = 'results')  
]