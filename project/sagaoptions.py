'''
Author: Scott Field
Version: 1.0
Date: 5/24/2024
Purpose:
store the list of possible choices for every useful list of literal types in saga
'''

import json #To convert the python dictionary to json data

#The available keywords for units and equipment
#Syntax is: (DB Value, User Value)
class Options:
    unitOptions = (
        ("Hero","Hero"),
        ("Hearthguard", "Hearthguard"),
        ("Warrior","Warrior"),
        ("Levy","Levy")
    )
    equipmentOptions = (
        #General Equipment Section
        ("Bows", "Bows"),
        ("Bows and Slings", "Bows and Slings"),
        ("Composite Bows", "Composite Bows"),
        ("Crossbows", "Crossbows"),
        ("Heavy Weapons", "Heavy Weapons"),
        ("Improvised Projectiles", "Improvised Projectiles"),
        ("Javelins", "Javelins"),
        ("Sarissa","Sarissa"),
        ("Slings", "Slings"),
        ("Unarmed","Unarmed"),

        #Horse + Equipment Section
        ("Horse","Horse"),
        ("Horse, Cataphract","Horse, Cataphract"),
        ("Horse, Composite Bows","Horse, Composite Bows"),
        ("Horse, Javelins","Horse, Javelins"),

        #Camel + Equipment Section
        ("Camel, Composite Bows","Camel, Composite Bows"),
        ("Camel, Javelins","Camel, Javelins"),

        #Represents No Special Equipment
        ("-","-"),
    )

#After this is Where Data Was Originally Intended to be Imported Into JavaScript, this code is currently unimplemented on the Python Side

#Function to shorten creation of unit:
def createUnit(sagaDice,cost,unitType,unitName,numModels,equipment,armourMelee,armourRanged,aggMelee,aggRanged,specialRules,isLegendary):
    return {
        "sagaDice" : sagaDice,
        "cost" : cost,
        "unitType" : unitType,
        "unitName" : unitName,
        "numModels" : numModels,
        "equipment" : equipment,
        "armourMelee" : armourMelee,
        "armourRanged" : armourRanged,
        "aggMelee" : aggMelee,
        "aggRanged" : aggRanged,
        "specialRules" : specialRules,
        "isLegendary" : isLegendary
    }

#The default values for a unit when creating a new faction, and when adding a new unit to a faction
class Default:
    units = {
        "Hero" : createUnit(sagaDice = 1, cost = 0, unitType = "Hero",unitName = "Warlord", numModels = 1, equipment = "-", armourMelee = 5, armourRanged = 5, aggMelee = 8, aggRanged = 0, specialRules = "-", isLegendary = False),
        "Hearthguard" : createUnit(1,1,"Hearthguard","Hearthguard",4,"-",5,5,2,0,"-",False),
        "Warrior" : createUnit(1,1,"Warrior","Warrior",8,"-",4,4,1,0,"-",False),
        "Levy" : createUnit(1,1,"Levy","Levy",12,"-",4,4,1,0,"-",False)
    }

#Wrap Data To Be Parsed To JSON
data = {
    "Options" : {
        "unitOptions": Options.unitOptions, 
        "equipmentOptions" : Options.equipmentOptions
    },
    "Default" : Default.units
}

#Attempt To Write The Data To A JSON file that will be used to send the data to the JavaScript File
with open("saga/static/saga/sagaoptions.json", "w") as jFile:
    json.dump(data, jFile, indent=4)
    