//Log if file has been accessed
console.log("edit.js loaded successfully");
//Track the rows to delete from the database (Global Variable)
let deleteRows = [];

//Function for deleting a faction
function submitDeleteForm(url) {
    var form = document.getElementById('factionForm');
    form.action = url;
    console.log("Delete Faction Button Pressed");
    form.submit();
}


function submitEditForm(url){
    var form = document.getElementById('factionForm');
    var deleteInputTag = document.getElementById('deleteRows');
    //Convert Array To String
    deleteInputTag.value = deleteRows.join(',');
    form.action = url;
    form.submit();
}


//Function To select Table Row for deletion on submit when Button Press
function deleteRow(event){
    //Find the closest row
    row = event.target.closest('tr');
    //Find the database Id of the Unit represented by that row
    inputTag = row.querySelector("input[name='unitId']");
    id = inputTag.value;
    //Get the specific delete button that was clicked
    deleteButton = event.target;

    //First check if the row is a new row (id === "new")
    if (id === "new"){
        row.remove();
    }
    //Check if the row is already grayed out
    else if (deleteRows.includes(id)){
        // If grayed out, revert the row to its original color
        row.style.backgroundColor = '';
        deleteButton.textContent = 'Delete';
        deleteButton.style.color = 'red';
        //Remove the row from the deleteRows array
        deleteRows.splice(deleteRows.indexOf(id), 1);    
    }else{
        //If not grayed out, gray out the row
        row.style.backgroundColor = 'grey';
        deleteButton.textContent = 'Cancel';
        deleteButton.style.color = 'black';
        //Add the row to the greyedOutRows array
        deleteRows.push(id);
    }
    //Push to the console which rows are to be deleted
    console.log("Delete Rows:", deleteRows)
}

//After document has loaded, run the rest of the JavaScript
document.addEventListener("DOMContentLoaded", function(){
    //Get Elements Section

    //Get the current Delete Buttons (Is not a const as new delete buttons may be added with their rows)
    deleteButtons = document.querySelectorAll(".deleteRow");

    //Get the form
    factionForm = document.getElementById("factionForm");

    //Form submission handler
    factionForm.addEventListener("submit", function(event) {
        //Prevent default form submission
        event.preventDefault();  
    });

    /*
    This section is for the Delete Button on selection it will turn the table row to be deleted grey
    however it will also switch to a cancel button that can reverse the deletion operation
    a row will only be submitted / deleted after the Save Changes button has been clicked
    */

    //Function To select Table Row for deletion on submit when Button Press
    function deleteRow(event){
        //Find the closest row
        row = event.target.closest('tr');
        //Find the database Id of the Unit represented by that row
        inputTag = row.querySelector("input[name='unitId']");
        id = inputTag.value;
        //Get the specific delete button that was clicked
        deleteButton = event.target;

        // Check if the row is already grayed out
        if (deleteRows.includes(id)){
            // If grayed out, revert the row to its original color
            row.style.backgroundColor = '';
            deleteButton.textContent = 'Delete';
            deleteButton.style.color = 'red';
            // Remove the row from the deleteRows array
            deleteRows.splice(deleteRows.indexOf(id), 1); 
        }else{
            // If not grayed out, gray out the row
            row.style.backgroundColor = 'grey';
            deleteButton.textContent = 'Cancel';
            deleteButton.style.color = 'black';
             // Add the row to the greyedOutRows array
            deleteRows.push(id);
        }
        //Push to the console which rows are to be deleted
        console.log("Delete Rows:", deleteRows)
    }

    //Get All Of The Delete Buttons (Is not a const as new delete buttons may be added / removed as new rows are added / removed)
    deleteButtons = document.querySelectorAll('.deleteRow');

    //Add The deleteRow event listener to each of the buttons
    deleteButtons.forEach(button => {
        button.addEventListener('click', deleteRow);
    });
});

/*
This is the section for dynamically adding new Units to the rows to then add to the table
*/

//Speed up default unit creation
function createUnit(sagaDice, cost, unitType, unitName, numModels, equipment, armourMelee, armourRanged, aggMelee, aggRanged, specialRules, isLegendary) {
    return {
      sagaDice: sagaDice,
      cost: cost,
      unitType: unitType,
      unitName: unitName,
      numModels: numModels,
      equipment: equipment,
      armourMelee: armourMelee,
      armourRanged: armourRanged,
      aggMelee: aggMelee,
      aggRanged: aggRanged,
      specialRules: specialRules,
      isLegendary: isLegendary
    };
}

//Get The Unit Stats to Add To The Row Depending on the button clicked
function addUnit(type){
    if (type === "Hero"){
        data = createUnit(1,0,"Hero","Warlord",1,"-",5,5,8,0,"-",false)   
    }else if (type === "Hearthguard"){
        data = createUnit(1,1,"Hearthguard","Hearthguard",4,"-",5,5,2,0,"-",false)
    }else if (type === "Warrior"){
        data = createUnit(1,1,"Warrior","Warrior",8,"-",4,4,1,0,"-",false)
    }else if (type === "Levy"){
        data = createUnit(1,1,"Levy","Levy",12,"-",4,4,1,0,"-",false)
    }else{
        console.log("Invalid Argument Passed By The Button")
        return;
    }
    addRow(data);
}

//Add a row to the table using JavaScript
function addRow(data){
    //Define Literals To Store Data That Was Difficult To Import (In version 2.0 this will be pulled from session storage)

    //Available types of units 
    const unitOptions = [
        ["Hero", "Hero"],
        ["Hearthguard", "Hearthguard"],
        ["Warrior", "Warrior"],
        ["Levy", "Levy"]
    ];

    //Available types of equipment
    const equipmentOptions = [
        // General Equipment Section
        ["Bows", "Bows"],
        ["Bows and Slings", "Bows and Slings"],
        ["Composite Bows", "Composite Bows"],
        ["Crossbows", "Crossbows"],
        ["Heavy Weapons", "Heavy Weapons"],
        ["Improvised Projectiles", "Improvised Projectiles"],
        ["Javelins", "Javelins"],
        ["Sarissa", "Sarissa"],
        ["Slings", "Slings"],
        ["Unarmed", "Unarmed"],
      
        // Horse + Equipment Section
        ["Horse", "Horse"],
        ["Horse, Cataphract", "Horse, Cataphract"],
        ["Horse, Composite Bows", "Horse, Composite Bows"],
        ["Horse, Javelins", "Horse, Javelins"],
      
        // Camel + Equipment Section
        ["Camel, Composite Bows", "Camel, Composite Bows"],
        ["Camel, Javelins", "Camel, Javelins"],
      
        // Represents No Special Equipment
        ["-", "-"]
      ];


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

    //Legendary Select Field
    const isLegendaryCell = document.createElement('td');
    const isLegendary = document.createElement('select');
    isLegendary.name = "isLegendary"

    trueOption = document.createElement('option');
    trueOption.value = "True";

    falseOption = document.createElement('option');
    falseOption.value = "False";
    falseOption.selected = true;
    
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
    cost.value = data["cost"];
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