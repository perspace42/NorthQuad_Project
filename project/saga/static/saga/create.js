//Log if file has been accessed
console.log("create.js loaded successfully");
//global variable that will store the data in the from the sagaoptoins.json file
let sagaOptions;

//Function to get the JSON file
async function getSagaOptions() {
    /*
    var scriptTag = document.currentScript;
    var optionsFileUrl = scriptTag.dataset.optionsFile;
    */
    var scriptTag = document.querySelector('script[src*="create.js"]');
    var optionsFileUrl = new URL('sagaoptions.json', scriptTag.src).href;

    try {
        const response = await fetch(optionsFileUrl);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching sagaoptions.json:', error);
        return null;
    }
}

//Function to assign the JSON file to the variable
async function assignSagaOptions() {
    sagaOptions = await getSagaOptions();
    console.log("sagaOptions: ",sagaOptions);
}



//Function for Saving Faction to database
function submitSaveForm(url){
    var form = document.getElementById('factionForm');
    form.action = url;
    console.log("Save Faction Button Pressed");
    form.submit()
}

//Function To delete table row when delete button pressed
function deleteRow(event){
    //Find the closest row
    row = event.target.closest('tr');
    //Then Remove it
    row.remove()
}

//After document has loaded, run the rest of the JavaScript
document.addEventListener('DOMContentLoaded', async function(){
    //Wait to load the necessary data
    await assignSagaOptions();
    //Add Units to Empty Faction On Load
    addUnit("Hero");
    addUnit("Hearthguard");
    addUnit("Warrior");
    addUnit("Levy");
});


/*
This is the section for dynamically adding new Units to the rows to then add to the table
*/
//Get The Unit Stats to Add To The Row Depending on the button clicked
function addUnit(type){
    var data;
    if (type === "Hero"){
        data = sagaOptions.Default.Hero;
    }else if (type === "Hearthguard"){
        data = sagaOptions.Default.Hearthguard;
    }else if (type === "Warrior"){
        data = sagaOptions.Default.Warrior;
    }else if (type === "Levy"){
        data = sagaOptions.Default.Levy;
    }else{
        console.log("Invalid Argument: ",type," passed by addUnit")
        return;
    }
    addRow(data);
}

//Add a row to the table using JavaScript
function addRow(data){
    //Available types of units 
    const unitOptions = sagaOptions.Options.unitOptions;

    //Available types of equipment
    const equipmentOptions = sagaOptions.Options.equipmentOptions;

    //Get The Table
    const table = document.getElementById('unitTable');

    //Create The Row
    const row = document.createElement('tr');

    //Shade Row To Flag To User That Row Is Newly Created
    row.style.backgroundColor = "cadetblue";

    //Row Id (To Flag To System That The Row Is Newly Created)  
    const unitId = document.createElement("input");
    unitId.type = "hidden";
    unitId.name = "unitId";
    unitId.value = "new";
    row.appendChild(unitId);
    
    //Unit Type
    const unitTypeCell = document.createElement('td');
    const unitType = document.createElement('select');
    unitType.name = 'unitType';
    
    unitOptions.forEach(list => {
        option = document.createElement('option');
        option.value = list[0];
        option.textContent = list[1];
        if (list[1] === data["unitType"]){
            option.selected = true;
        }
        unitType.appendChild(option);
    });

    unitTypeCell.appendChild(unitType);
    row.appendChild(unitTypeCell);
    
    //Unit Name
    const unitNameCell = document.createElement('td');
    const unitName = document.createElement('input');
    unitName.type = 'text';
    unitName.name = 'unitName';
    unitName.value = data["unitName"];
    unitNameCell.appendChild(unitName);
    row.appendChild(unitNameCell);

    //Saga Dice
    const sagaDiceCell = document.createElement('td');
    const sagaDice = document.createElement('input');
    sagaDice.type = 'number';
    sagaDice.name = 'sagaDice';
    sagaDice.className = 'shrinkInput';
    sagaDice.min = '0';
    sagaDice.value = data["sagaDice"];
    sagaDiceCell.appendChild(sagaDice);
    row.appendChild(sagaDiceCell);

    //Model Number
    const numModelsCell = document.createElement('td');
    const numModels = document.createElement('input');
    numModels.type = 'number';
    numModels.name = 'numModels';
    numModels.className = 'shrinkInput';
    numModels.min = '0';
    numModels.value = data["numModels"];
    numModelsCell.appendChild(numModels);
    row.appendChild(numModelsCell);

    //Equipment Options
    const equipmentCell = document.createElement('td');
    const equipment = document.createElement('select');
    equipment.name = 'equipment';
    
    equipmentOptions.forEach(list => {
        option = document.createElement('option');
        option.value = list[0];
        option.textContent = list[1];
        if (list[1] === data["equipment"]) {
            option.selected = true;
        }
        equipment.appendChild(option);
    });
    
    equipmentCell.appendChild(equipment);
    row.appendChild(equipmentCell);

    //Armour Melee
    const armourMeleeCell = document.createElement('td');
    const armourMelee = document.createElement('input');
    armourMelee.type = 'number';
    armourMelee.name = 'armourMelee';
    armourMelee.className = 'shrinkInput';
    armourMelee.min = '0';
    armourMelee.value = data["armourMelee"];
    armourMeleeCell.appendChild(armourMelee);
    row.appendChild(armourMeleeCell);

    //Armour Ranged
    const armourRangedCell = document.createElement('td');
    const armourRanged = document.createElement('input');
    armourRanged.type = 'number';
    armourRanged.name = 'armourRanged';
    armourRanged.className = 'shrinkInput';
    armourRanged.min = '0';
    armourRanged.value = data["armourRanged"];
    armourRangedCell.appendChild(armourRanged);
    row.appendChild(armourRangedCell);

    //Aggression Melee
    const aggMeleeCell = document.createElement('td');
    const aggMeleeInput = document.createElement('input');
    aggMeleeInput.type = 'number';
    aggMeleeInput.name = 'aggMelee';
    aggMeleeInput.className = 'shrinkInput';
    aggMeleeInput.min = '0';
    aggMeleeInput.step = '0.01';
    aggMeleeInput.value = data["aggMelee"];
    aggMeleeCell.appendChild(aggMeleeInput);
    row.appendChild(aggMeleeCell);

    //Agression Ranged
    const aggRangedCell = document.createElement('td');
    const aggRangedInput = document.createElement('input');
    aggRangedInput.type = 'number';
    aggRangedInput.name = 'aggRanged';
    aggRangedInput.className = 'shrinkInput';
    aggRangedInput.min = '0';
    aggRangedInput.step = '0.01';
    aggRangedInput.value = data["aggRanged"];
    aggRangedCell.appendChild(aggRangedInput);
    row.appendChild(aggRangedCell);

    //Special Rules
    const specialRulesCell = document.createElement('td');
    const specialRulesTextarea = document.createElement('textarea');
    specialRulesTextarea.name = 'specialRules';
    specialRulesTextarea.textContent = data["specialRules"];
    specialRulesCell.appendChild(specialRulesTextarea);
    row.appendChild(specialRulesCell);

    //Legendary Checkbox
    const isLegendaryCell = document.createElement('td');
    const isLegendary = document.createElement('select');
    isLegendary.name = "isLegendary"

    trueOption = document.createElement('option');
    trueOption.value = "True";
    trueOption.textContent = "True";

    falseOption = document.createElement('option');
    falseOption.value = "False";
    falseOption.textContent = "False"

    if(!data.isLegendary){
        falseOption.selected = true;
    }else{
        trueOption.selected = true;
    }

    isLegendary.appendChild(trueOption)
    isLegendary.appendChild(falseOption)
    isLegendaryCell.appendChild(isLegendary);
    row.appendChild(isLegendaryCell);

    //Cost
    const costCell = document.createElement('td');
    const cost = document.createElement('input');
    cost.type = 'number';
    cost.name = 'cost';
    cost.className = 'shrinkInput';
    cost.value = data['cost'];
    costCell.appendChild(cost);
    row.appendChild(costCell);

    //Delete Button
    const deleteButtonCell = document.createElement('td');
    const deleteButton = document.createElement('button');
    deleteButton.type = 'button';
    deleteButton.className = 'deleteRow';
    deleteButton.textContent = 'Delete';
    //Add The Ability To Delete The Row
    deleteButton.addEventListener('click', deleteRow)
    deleteButtonCell.appendChild(deleteButton);
    row.appendChild(deleteButtonCell);

    //Add Finished Row To Table
    table.appendChild(row);
}