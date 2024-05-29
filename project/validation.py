'''
Author: Scott Field
Version: 1.0
Date: 5/28/2024
Purpose:
Check a given saga faction and unit for valid data types
'''

from sagaoptions import Options as So

#Return a validated list of unit fields, or an empty list if a field is incorrect
def validate(sagaDice,cost,unitType,unitName,numModels,equipment,armourMelee,armourRanged,aggMelee,aggRanged,specialRules,isLegendary):
    values = {}
    validItems = []
    #Attempt to Convert Strings into valid data types
    try:
        values["sagaDice"] = int(sagaDice)
        values["cost"] = int(cost)
        #Get possible values for unit type
        for tuple in So.unitOptions:
            validItems.append(tuple[1])
        #After getting valid values check if the type is one of them
        assert unitType in validItems, "Unit Type Out Of Range"
        values["unitType"] = unitType
       
        #No validation on unit name
        values["unitName"] = unitName

        values["numModels"] = int(numModels)

        #Get possible values for unit equipment
        for tuple in So.equipmentOptions:
            validItems.append(tuple[1])
        #After getting valid values check if the equipment is one of them
        assert equipment in validItems, "Unit Equipment Out Of Range"
        values["equipment"] = equipment

        values["armourMelee"] = int(armourMelee)
        values["armourRanged"] = int(armourRanged)
        values["aggMelee"] = float(aggMelee)
        values["aggRanged"] = float(aggRanged)
        values["specialRules"] = specialRules

        #Test if isLegendary String can be converted to a valid boolean
        assert(isLegendary == "True" or isLegendary == "False"), "Unit Legendary status is neither True nor False"
        values["isLegendary"] = eval(isLegendary)

    except (Exception, AssertionError) as e:
        values.clear()
        print("A problem occurred during validation:",e)

    finally:
        return values
