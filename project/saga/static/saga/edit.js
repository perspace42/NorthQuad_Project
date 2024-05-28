//Log if file has been accessed
console.log("edit.js loaded successfully");

/*
This function is to retrieve a cookie (the CSRF token), which is needed
to validate post requests
*/

/*
function getCSRF() {
    const cookies = document.cookie.split('; ');
    for (let i = 0; i < cookies.length; i++) {
        const [name, value] = cookies[i].split('=');
        if (name === "csrfToken") {
            return decodeURIComponent(value);
        }
    }
  return null;
}
*/

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
    function deleteRow(event) {
        row = event.target.closest('tr');
        button = event.target;

        // Check if the row is already grayed out
        if (deleteRows.includes(row)) {
            // If grayed out, revert the row to its original color
            row.style.backgroundColor = '';
            button.textContent = 'Delete';
            button.style.color = 'red';
            // Remove the row from the deleteRows array
            deleteRows.splice(deleteRows.indexOf(row), 1); 
        } else {
            // If not grayed out, gray out the row
            row.style.backgroundColor = 'grey';
            button.textContent = 'Cancel';
            button.style.color = 'black';
             // Add the row to the greyedOutRows array
            deleteRows.push(row);
        }
    }

    //Get All Of The Delete Buttons (Is not a const as new delete buttons may be added / removed as new rows are added / removed)
    deleteButtons = document.querySelectorAll('.deleteRow');

    //Add The deleteRow event listener to each of the buttons
    deleteButtons.forEach(button => {
        button.addEventListener('click', deleteRow);
    });

    
    /*
    This is the section for the form and its custom submission handlers
    The first is for saving changes to a faction and the second is for
    permenantly deleting a facition
    */
    /*
    factionForm.addEventListener('submit', function(event) {
        //prevent the default form submission
        event.preventDefault(); 
        //If the Save Changes button is clicked
        if (event.submitter === saveSubmit){
            console.log("Save Changes Pressed");
            // Code to handle form submission and save changes to the database
        }
        
        else if(event.submitter === deleteSubmit){
            console.log("Delete Faction Pressed");
            
            //Attempt to send data to server
            fetch(`/saga/delete/${factionId.value}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRF(),
                },
            })
            //Get response from server
            .then(response => {
                if (response.ok) {
                    console.log('Faction deleted successfully');
                } else {
                    //If a problem occurred display the response
                    console.error('Error deleting faction',response);
                }
            })
            //If There is an error output it
            .catch(error => {
                console.error('Error:', error);
            });
        }
        
        //Otherwise if neither approved button submitted the form something went wrong
        else {//Otherwise if neither approved button submitted the form something went wrong
            console.log(event.submitter, "somehow submitted the form, check and correct the code near that element");
        }
    })
    */


});