'''
Author: Scott Field
Date: 5/24/2024
Version: 1.0
Purpose:
Defines the model classes that are used to generate the SQL database
'''

from django.db import models
# Create your models here.
from sagaoptions import Options as So

#Faction Model
class Faction(models.Model):
    #The id must be a char here for Faction because: the (Unit) factionName will not accept the (Faction) name as a foreign key
    id = models.AutoField(primary_key=True)
    #The name of the Saga Faction is unique as no two factions can have the same name
    name = models.CharField(max_length = 30)
    description = models.TextField(default = "")
    specialRules = models.TextField(default = "-")

    #String Representation
    def __str__(self):
        return self.name

#Unit Within Faction Model
class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    #The amount of dice a unit generates at the start of the turn
    sagaDice = models.PositiveIntegerField(default = 1)

    #The cost to recruit a unit
    cost = models.PositiveIntegerField(default = 1)

    #Can be: Hero, Hearthguard, Warrior, Levy (default is Hero)
    unitType = models.CharField(max_length = 20, default = "Hearthguard", choices=So.unitOptions)

    #The name of a unit
    unitName = models.CharField(max_length = 50, default = "Hearthguard")

    #The number of models a unit contains
    numModels = models.PositiveIntegerField(default = 4)

    #Equipment is a list of any equipment unit contains
    equipment = models.CharField(max_length = 50, default = "-", choices=So.equipmentOptions)
    
    #Armour in Saga must be a positive integer
    armourMelee = models.PositiveIntegerField(default = 5)
    armourRanged = models.PositiveIntegerField(default = 5)

    #Agression in Saga can be a fractional number
    aggMelee = models.FloatField(default = 2)
    aggRanged = models.FloatField(default = 0)

    #Special rules include rules added by equipment
    specialRules = models.TextField(default = "-")

    #If the unit is a legendary unit
    isLegendary = models.BooleanField(default = False)

    #Link Hero to the owning Faction (If Faction Removed, Unit is Also Removed)
    factionId = models.ForeignKey(Faction, on_delete = models.CASCADE)

    #String Representation
    def __str__(self):
        #Ensure that equipment is only added to name if there is any equipment to add
        return self.unitName if self.equipment == "-" else self.unitName + " " +  self.equipment

    

