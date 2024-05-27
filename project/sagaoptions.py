'''
Author: Scott Field
Version: 1.0
Date: 5/24/2024
Purpose:
store the list of possible choices for every list of literal types in saga
'''

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