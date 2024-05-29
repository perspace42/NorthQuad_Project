'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Defines the views for: Create, Read, Update, Delete, for the website
(The Get, Post, Update and Delete Requests)
'''


from django.shortcuts import get_object_or_404, render, redirect #shorten instructions
from django.urls import reverse #enable generating urls from routes

from .models import Faction, Unit
from sagaoptions import Options
from validation import validate

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
    print(faction.first)
    #If Any Factions Exist With The Given FactionId
    if faction.count() > 0:
        print("We're digging for units")
        #If so get the units in that faction whose factionId matches the foreign key: id (factionId__id) from Faction
        unitList = Unit.objects.filter(factionId__id = factionId)
        #If antything is in the unit list
        if unitList.count() > 0:
            print("We found units")
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
            print("No units in faction")
            context = {
                "faction" : faction
            }
            return render(request, "saga/results.html", context)
    
    #Error Non Existent Faction
    else:
        print("no faction found")
        #Redirect To Home Page 
        return redirect(reverse('saga:index'))

#Edit/Create Page, (Edit/Delete Exiting Faction)

#If No Faction Supplied (Create New Faction)
def create(request):
    context = {
        "options" : Options
    }
    
    return render(request,"saga/create.html", context)

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
        #Return to home page on success (Will change to success message later)
        return redirect(reverse("saga:index"))
    
    #Return to create page on failure (Will change to failure message later)
    return redirect(reverse("saga:create"))    


#Push Changes To Faction (From Edit Page)
def editPush(request, factionId):
    #Get Faction to Push Changes Too
    try:
        faction = get_object_or_404(Faction,id = factionId)
    except:
        #Will Change to error message later
        print("Faction Not Found")
        return redirect(reverse("saga:index"))

    #If Faction Exists and Data has been posted from a form
    if request.method == "POST":
        #Pull Data From Request (pulls by name field)

        #Faction Data
        factionName = request.POST.get('fName')
        factionDescription = request.POST.get('fDescription')
        factionSpecial = request.POST.get('fSpecial')

        #Unit List Data (By Row)
        idList = request.POST.getlist('unitId')
        typeList = request.POST.getlist('unitType')
        nameList = request.POST.getlist('unitName')
        diceList = request.POST.getlist('sagaDice')
        modelList = request.POST.getlist('numModels')
        equipmentList = request.POST.getlist('equipment')
        armourMeleeList = request.POST.getlist('armourMelee')
        armourRangedList = request.POST.getlist('armourRanged')
        aggMeleeList = request.POST.getlist('aggMelee')
        aggRangedList = request.POST.getlist('aggRanged')
        specialList = request.POST.getlist('specialRules')
        legendaryList = request.POST.getlist('isLegendary')
        costList = request.POST.getlist('cost')

        #Note operations will only be executed if no errors occur

        #To Store Units To Be Added To The Database
        newUnitsList = []
        #To Store Units To Be Edited In The Database
        updateUnitsList = []
        #To Store Units To Be Deleted From The Database
        deleteUnitsList = []

        #List of Units To Be Deleted (By ID that are to be deleted)
        deleteString = request.POST.get('deleteRows')
        if (deleteString != ""):
            deleteRows = deleteString.split(",")
        else:
            deleteRows = []

        #Ensure Faction Data is not empty
        for factionValues in ((factionName,factionDescription,factionSpecial)):
            if factionValues.strip() == "":
                print("One of the faction values is empty")
                return redirect(reverse("saga:index"))

        #Add Changes to Faction Fields
        faction.name = factionName
        faction.description = factionDescription 
        faction.specialRules = factionSpecial

        #Remove unit data from units that will be deleted, from the form
        for id in deleteRows:
            index = idList.index(id)
            del idList[index]
            del typeList[index]
            del nameList[index]
            del diceList[index]
            del modelList[index]
            del equipmentList[index]
            del armourMeleeList[index]
            del armourRangedList[index]
            del aggMeleeList[index]
            del aggRangedList[index]
            del specialList[index]
            del legendaryList[index]
            del costList[index]

        #Delete units from database
        for string in deleteRows:
            #Convert Data
            deleteId = int(string)
            #Delete From Faction
            try:
                unit = get_object_or_404(Unit, id = deleteId)
                #Add unit to the deletion list
                deleteUnitsList.append(unit)
            except:
                print("Unit To Delete Not Found")
                #This does not redirect as trying to delete a unit that isn't present, indicates it has already been deleted
                return redirect(reverse("saga:index"))
            
        #Update and Insert Each Other Rows
        for index in range(len(idList)):
            id = idList[index]
            #Get Values (Validation Function Either Returns Valid Values or an Empty Dictionary)
            values = validate(
                sagaDice = diceList[index],
                cost = costList[index],
                unitType = typeList[index],
                unitName = nameList[index],
                numModels = modelList[index],
                equipment = equipmentList[index],
                armourMelee = armourMeleeList[index],
                armourRanged = armourRangedList[index],
                aggMelee = aggMeleeList[index],
                aggRanged = aggRangedList[index],
                specialRules = specialList[index],
                isLegendary = legendaryList[index],
            )
                
            #INSERT OPERATION
            if id == "new":
                #Create the new unit
                newUnit = Unit(
                    sagaDice = values["sagaDice"],
                    cost = values["cost"],
                    unitType = values["unitType"],
                    unitName = values["unitName"],
                    numModels = values["numModels"],
                    equipment = values["equipment"],
                    armourMelee = values["armourMelee"],
                    armourRanged = values["armourRanged"],
                    aggMelee = values["aggMelee"],
                    aggRanged = values["aggRanged"],
                    specialRules = values["specialRules"],
                    isLegendary = values["isLegendary"],
                    factionId = faction
                )
                #Add unit to the add list
                newUnitsList.append(newUnit)

            #UPDATE OPERATION 
            else:
                #First try to get the unit that will be updated
                try:
                    unitId = int(id)
                    unit = get_object_or_404(Unit, id = unitId)
                except:
                    print(f"Unit With ID: {id} not found")
                    return redirect(reverse("saga:index"))
                
                #Then update the unit if the values are correct
                if values:
                    unit.sagaDice = values["sagaDice"]
                    unit.cost = values["cost"]
                    unit.unitType = values["unitType"]
                    unit.unitName = values["unitName"]
                    unit.numModels = values["numModels"]
                    unit.equipment = values["equipment"]
                    unit.armourMelee = values["armourMelee"]
                    unit.armourRanged = values["armourRanged"]
                    unit.aggMelee = values["aggMelee"]
                    unit.aggRanged = values["aggRanged"]
                    unit.specialRules = values["specialRules"]
                    unit.isLegendary = values["isLegendary"]

                    #Then save changes
                    updateUnitsList.append(unit)
                #If no valid values provided, redirect
                else:
                    return redirect(reverse("saga:index"))


        #Save Changes Section
        #This section is only reached if no errors have occurred accessing and validating the data
        for deleteUnit in deleteUnitsList:
            deleteUnit.delete()

        for updateUnit in updateUnitsList:
            updateUnit.save()

        for newUnit in newUnitsList:
            newUnit.save()

        #Remember to save faction changes as well
        faction.save()

        #Return to view page on success (Will change to success message later)
        return redirect(reverse("saga:results",args=[factionId]))

    #Return to home page on failure (Will change to failure message later)
    return redirect(reverse("saga:index"))

#Push New Faction To Database (From Create Page)
def createPush(request):

    #If Faction Exists and Data has been posted from a form
    if request.method == "POST":
        #Pull Data From Request (pulls by name field)

        #Faction Data
        factionName = request.POST.get('fName')
        factionDescription = request.POST.get('fDescription')
        factionSpecial = request.POST.get('fSpecial')

        #Unit List Data (By Row)
        idList = request.POST.getlist('unitId')
        typeList = request.POST.getlist('unitType')
        nameList = request.POST.getlist('unitName')
        diceList = request.POST.getlist('sagaDice')
        modelList = request.POST.getlist('numModels')
        equipmentList = request.POST.getlist('equipment')
        armourMeleeList = request.POST.getlist('armourMelee')
        armourRangedList = request.POST.getlist('armourRanged')
        aggMeleeList = request.POST.getlist('aggMelee')
        aggRangedList = request.POST.getlist('aggRanged')
        specialList = request.POST.getlist('specialRules')
        legendaryList = request.POST.getlist('isLegendary')
        costList = request.POST.getlist('cost')

        #Note operations will only be executed if no errors occur

        #To Store Units To Be Added To The Database
        newUnitsList = []

        #Create Faction To Push Changes Too
        faction = Faction(
            name = factionName,
            description = factionDescription,
            specialRules = factionSpecial
        )
   
        #Check Each Of The Rows For Valid Values
        for index in range(len(idList)):
            #Get Values (Validation Function Either Returns Valid Values or an Empty Dictionary)
            values = validate(
                sagaDice = diceList[index],
                cost = costList[index],
                unitType = typeList[index],
                unitName = nameList[index],
                numModels = modelList[index],
                equipment = equipmentList[index],
                armourMelee = armourMeleeList[index],
                armourRanged = armourRangedList[index],
                aggMelee = aggMeleeList[index],
                aggRanged = aggRangedList[index],
                specialRules = specialList[index],
                isLegendary = legendaryList[index],
            )
                
            #Insert Operation
            #Create the new unit
            newUnit = Unit(
                sagaDice = values["sagaDice"],
                cost = values["cost"],
                unitType = values["unitType"],
                unitName = values["unitName"],
                numModels = values["numModels"],
                equipment = values["equipment"],
                armourMelee = values["armourMelee"],
                armourRanged = values["armourRanged"],
                aggMelee = values["aggMelee"],
                aggRanged = values["aggRanged"],
                specialRules = values["specialRules"],
                isLegendary = values["isLegendary"],
                factionId = faction
            )  
            newUnitsList.append(newUnit)

        #Save Changes Section
        #This section is only reached if no errors have occurred accessing and validating the data

        #Faction must be saved before units are saved
        faction.save()

        #Save units as well
        for newUnit in newUnitsList:
            newUnit.save()

        #Return to view page on success (Will change to success message later)
        return redirect(reverse("saga:results",kwargs = {"factionId" : faction.id}))

    #Return to home page on failure (Will change to failure message later)
    return redirect(reverse("saga:index"))