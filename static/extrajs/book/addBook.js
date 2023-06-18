

var book = document.getElementById("book")



function checkRequirements()
{
    
    if (book.value=='')
    {
        alert("Please select a Book")
    }
    else
    {
        document.getElementById("AddBook").click()
    }
    
}

var btn = document.getElementById("btn-js");
// add event listener for the button, for action "click"
btn.addEventListener("click", checkRequirements);