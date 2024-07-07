import * as sagaLibrary from "./library.js";

//Log if file has been accessed
console.log("edit.js loaded successfully");


//Function for deleting a faction
function submitDeleteForm(url) {
    var form = document.getElementById('factionForm');
    form.action = url;
    console.log("Delete Faction Button Pressed");
    form.submit();
}
//add to global scope
window.submitDeleteForm = submitDeleteForm;

//Function for editing a faction
function submitEditForm(url){
    var form = document.getElementById('factionForm');
    //This is a hidden input tag that stores the deleted rows
    var deleteInputTag = document.getElementById('deleteRows');
    //Convert Array To String
    deleteInputTag.value = sagaLibrary.deleteRowsList.join(',');
    form.action = url;
    form.submit();
}
//add to global scope
window.submitEditForm = submitEditForm;

//addUnit == sagaLibrary.addUnit in global scope
window.addUnit = sagaLibrary.addUnit


//After document has loaded, run the rest of the JavaScript
document.addEventListener('DOMContentLoaded', async function(){
    //Wait to load the necessary data
    await sagaLibrary.assignSagaOptions("edit.js","sagaoptions.json");
    //Get Elements Section

    //Get the current Delete Buttons (Is not a const as new delete buttons may be added with their rows)
    var deleteButtons = document.querySelectorAll(".deleteRow");

    //Get the form
    var factionForm = document.getElementById("factionForm");

    //Form submission handler
    factionForm.addEventListener("submit", function(event) {
        //Prevent default form submission
        event.preventDefault();  
    });

    //Get All Of The Delete Buttons (Is not a const as new delete buttons may be added / removed as new rows are added / removed)
    deleteButtons = document.querySelectorAll('.deleteRow');

    //Add The deleteRow event listener to each of the buttons
    deleteButtons.forEach(button => {
        button.addEventListener('click', sagaLibrary.deleteRow);
    });
});

