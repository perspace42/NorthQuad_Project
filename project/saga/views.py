'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Defines the views for: Create, Read, Update, Delete, for the website
(The Get, Post, Update and Delete Requests)
'''


from django.shortcuts import render, redirect #shorten instructions
from django.urls import reverse #enable generating urls from routes

from .models import Faction, Unit
from sagaoptions import Default, Options

# Views Section

#Home Page, (GET Faction)
def index(request):
    #Get the factions in alphabetical order
    factionList = Faction.objects.order_by('name')
    context = {"factionList" : factionList}
    return render(request,"saga/index.html", context)

#Results View Page, (GET Units that are in a Faction)
def results(request,factionId):   
    #Get Faction From FactionId
    faction = Faction.objects.filter(id = factionId)
    #If Any Factions Exist With The Given FactionId
    if faction.count() > 0:
        #If so get the units in that faction whose factionId matches the foreign key: id (factionId__id) from Faction
        unitList = Unit.objects.filter(factionId__id = factionId)
        #If antything is in the unit list
        if unitList.count() > 0:
            #Split unit list into alphabetically ordered unit types
            heroList = Unit.objects.filter(factionId__id = factionId, unitType = "Hero").order_by("unitName")
            hearthguardList = Unit.objects.filter(factionId__id = factionId, unitType = "Hearthguard").order_by("unitName")
            warriorList = Unit.objects.filter(factionId__id = factionId, unitType = "Warrior").order_by("unitName")
            levyList = Unit.objects.filter(factionId__id = factionId, unitType = "Levy").order_by("unitName")

            #The order of the unitSet will determine the order in which table units are displayed by type
            unitSet = [heroList,hearthguardList,warriorList,levyList]
            
            context = {
                "unitSet" : unitSet, 
                "faction" : faction
                }
            return render(request, "saga/results.html", context)
        
        #Faction Exists, Contains No Units
        else:
            return render(request, "saga/results.html")
    
    #Error Non Existent Faction
    else:
        #Redirect To Home Page (Must be namespaced due to app name)
        return redirect(reverse('saga:index'))

#Edit/Create Page, (Edit/Delete Exiting Faction)

#If No Faction Supplied (Create New Faction)
def create(request):
    context = {
        "defaultUnits" : Default.units,
        "options" : Options
    }
    return render(request,"saga/edit.html", context)

#If Faction Supplied (Edit Existing Faction)
def edit(request,factionId):
    #Get Faction From FactionId
    faction = Faction.objects.filter(id = factionId)
    #If Any Factions Exist With The Given FactionId
    if faction.count() > 0:
        #If so get the units in that faction whose factionId matches the foreign key: id (factionId__id) from Faction
        unitList = Unit.objects.filter(factionId__id = factionId)
        #If antything is in the unit list
        if unitList.count() > 0:
            #Split unit list into alphabetically ordered unit types
            heroList = Unit.objects.filter(factionId__id = factionId, unitType = "Hero").order_by("unitName")
            hearthguardList = Unit.objects.filter(factionId__id = factionId, unitType = "Hearthguard").order_by("unitName")
            warriorList = Unit.objects.filter(factionId__id = factionId, unitType = "Warrior").order_by("unitName")
            levyList = Unit.objects.filter(factionId__id = factionId, unitType = "Levy").order_by("unitName")

            #The order of the unitSet will determine the order in which table units are displayed by type
            unitSet = [heroList,hearthguardList,warriorList,levyList]
            
            context = {
                "unitSet" :unitSet, 
                "faction" : faction,
                "options" : Options
                }
            return render(request, "saga/edit.html", context)
    
    #Error Non Existent Faction
    else:
        #Redirect To Create Page (Must be namespaced due to app name)
        return redirect(reverse('saga:create'))


#Delete Faction (From Edit Page)
def delete(request,factionId):
    #Get Faction To Delete
    faction = Faction.objects.filter(id = factionId)
    #If Faction Exists and Data has been posted from a form
    if faction.count() > 0 and request.method == 'POST':
        #Delete the faction
        faction.delete()
        #Return to create page on success (Will change to success message later)
        return redirect(reverse("saga:create"))
    
    #Return to home page on failure (Will change to failure message later)
    return redirect(reverse("saga:index"))    


#Push Changes To Faction (From Edit Page)
def push(request,factionId):
    pass