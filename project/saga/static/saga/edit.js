//Log if file has been accessed
console.log("edit.js loaded successfully");

function submitDeleteForm(url) {
    var form = document.getElementById('factionForm');
    form.action = url;
    console.log("Delete Faction Button Pressed")
    form.submit();
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

    //Track the rows to delete from the database
    let deleteRows = [];

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