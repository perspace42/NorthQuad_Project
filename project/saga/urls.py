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
    #ex: /saga/results/1
    path("results/<int:factionId>",views.results, name = 'results'),
    #ex: /saga/create/
    path("create/", views.create, name = 'create'),
    #ex: /saga/edit/1
    path("edit/<int:factionId>", views.edit, name = 'edit'),  
    #ex: /saga/delete/1
    path("delete/<int:factionId>", views.delete, name = 'delete'),
    #ex: /saga/edit/push/
    path("edit/push/<int:factionId>",views.editPush, name = "editPush"),
    #ex: /saga/create/push
    path("create/push/",views.createPush, name = "createPush")
]