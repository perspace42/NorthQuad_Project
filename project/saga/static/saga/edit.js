//Log if file has been accessed
console.log("edit.js loaded successfully");

//After document has loaded, run the rest of the JavaScript
document.addEventListener('DOMContentLoaded', function(){
    //Get Elements Section

    //Get CSRF Token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    //Get the current Delete Buttons (Is not a const as new delete buttons may be added with their rows)
    deleteButtons = document.querySelectorAll('.deleteRow');
    //Get the page form
    factionForm = document.getElementById("factionForm")

    /*
    This section is for the Delete Button on selection it will turn the table row to be deleted grey
    however it will also switch to a cancel button that can reverse the deletion operation
    a row will only be submitted / deleted after the Save Changes button has been clicked
    */

    //Track the rows to delete from the database
    let deleteRows = [];

    //Function To select Table Row for deletion on submit when Button Press
    function deleteRow(event) {
        row = event.target.closest('tr');
        button = event.target;

        // Check if the row is already grayed out
        if (deleteRows.includes(row)) {
            // If grayed out, revert the row to its original color
            row.style.backgroundColor = '';
            button.textContent = 'Delete';
            button.style.color = 'red';
            deleteRows.splice(deleteRows.indexOf(row), 1); // Remove the row from the deleteRows array
        } else {
            // If not grayed out, gray out the row
            row.style.backgroundColor = 'grey';
            button.textContent = 'Cancel';
            button.style.color = 'black';
            deleteRows.push(row); // Add the row to the greyedOutRows array
        }
    }

    //Get All Of The Delete Buttons (Is not a const as new delete buttons may be added / removed as new rows are added / removed)
    deleteButtons = document.querySelectorAll('.deleteRow');

    //Add The deleteRow event listener to each of the buttons
    deleteButtons.forEach(button => {
        button.addEventListener('click', deleteRow);
    });

    /*This is the section for the form and its custom submission handler */
    factionForm.addEventListener('submit', function(event) {
        //prevent the default form submission
        event.preventDefault(); 
      });

});