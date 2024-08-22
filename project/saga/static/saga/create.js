import * as sagaLibrary from "./library.js";
//Log if file has been accessed
console.log("create.js loaded successfully");

//Function for Saving Faction to database
function submitSaveForm(url){
    if (window.confirm("Are you sure you want to create the faction?")){
        console.log("I have been run");
        var form = document.getElementById('factionForm');
        form.action = url;
        console.log("Save Faction Button Pressed");
        form.submit();
    }
}
//Expose to global scope
window.submitSaveForm = submitSaveForm;

//addUnit == sagaLibrary.addUnit in global scope
window.addUnit = sagaLibrary.addUnit

//After document has loaded, run the rest of the JavaScript
document.addEventListener('DOMContentLoaded', async function(){
    //Wait to load the necessary data
    await sagaLibrary.assignSagaOptions("create.js","sagaoptions.json");
    //Add Units to Empty Faction On Load
    sagaLibrary.addUnit("Hero");
    sagaLibrary.addUnit("Hearthguard");
    sagaLibrary.addUnit("Warrior");
    sagaLibrary.addUnit("Levy");    
});

