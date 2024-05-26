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
def results(request,factionId):   
    #Check if a faction is in the request
    if factionId:
        #If so get the units in that faction and the faction name
        unitList = Unit.objects.filter(factionId = factionId)
        faction = Faction.objects.filter(id = factionId)
        #If antything is in the list
        if unitList:
            context = {"unitList" : unitList, "faction" : faction}
            return render(request, "saga/results.html", context)
        else:
            #return render(request,"saga/results.html", context = {"unitList" : unitList})
            raise Http404("Error no units in UnitList")
    else:
        return render(request, "saga/results.html")

#Edit/Create Page, (Edit Exiting Faction, Delete Faction)