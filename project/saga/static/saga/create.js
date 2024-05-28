//Log if file has been accessed
console.log("create.js loaded successfully");

//Function for Saving Faction to database
function submitSaveForm(url){
    var form = document.getElementById('factionForm');
    form.action = url;
    console.log("Save Faction Button Pressed");
    form.submit()
}

//After document has loaded, run the rest of the JavaScript
document.addEventListener('DOMContentLoaded', function(){
    //Get Elements Section

    //Get the current Delete Buttons (Is not a const as new delete buttons may be added with their rows)
    deleteButtons = document.querySelectorAll('.deleteRow');
    //Get the page form
    const factionForm = document.getElementById("factionForm");
    //Get the delete faction button
    const deleteSubmit = document.getElementById("deleteSubmit");
    //Get the save changes button
    const saveSubmit = document.getElementById("saveSubmit");
    //Get the faction id
    const factionId = document.getElementById('factionId');

    /*
    This section is for the Delete Button on selection it will turn the table row to be deleted grey
    however it will also switch to a cancel button that can reverse the deletion operation
    a row will only be submitted / deleted after the Save Changes button has been clicked
    */

    //Function To delete table row when delete button pressed
    //This sel
    function deleteRow(event){
        //Find the closest row
        row = event.target.closest('tr');
        //Then Remove it
        row.remove()
    }

    //Get All Of The Delete Buttons (Is not a const as new delete buttons may be added / removed as new rows are added / removed)
    deleteButtons = document.querySelectorAll('.deleteRow');

    //Add The deleteRow event listener to each of the buttons
    deleteButtons.forEach(button => {
        button.addEventListener('click', deleteRow);
    });
});