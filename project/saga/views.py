'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Defines the views for: Create, Read, Update, Delete, for the website
(The Get, Post, Update and Delete Requests)
'''

from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect #Get / Send HttpResponse
from django.http import Http404 #Error Message
from django.shortcuts import render, get_object_or_404 #Shorten Instructions
from django.urls import reverse

from .models import Faction,Unit


# Create your views here.

#Home Page, (GET Faction)
def index(request):
    #Get the factions in alphabetical order
    factionList = Faction.objects.order_by('name')
    context = {"factionList" : factionList}
    return render(request,"saga/index.html", context)

#Results View Page, (GET Units that are in a Faction)
def results(request, factionId):
    #Get the units belonging to a specific faction
    unitList = Unit.objects
    if unitList:
        unitList = unitList.filter(id == factionId)
        context = {"unitList" : unitList}
        return render(request, "saga/results.html", context)
    else:
        raise Http404("Error no units in UnitList")

#Edit/Create Page, (Edit Exiting Faction, Delete Faction)