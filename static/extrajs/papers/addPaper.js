

var paper = document.getElementById("paper")



function checkRequirements()
{
    
    if (paper.value == '')
    {
        alert("Please select a Paper")
    }
    else
    {
        document.getElementById("AddPaper").click()
    }
    
}

var btn = document.getElementById("btn-js");
// add event listener for the button, for action "click"
btn.addEventListener("click", checkRequirements);