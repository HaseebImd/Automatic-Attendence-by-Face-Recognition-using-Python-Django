

var inputTitle = document.getElementById("inputTitle")
var option1 = document.getElementById("inputOption1")
var option2 = document.getElementById("inputOption2")
var option3 = document.getElementById("inputOption3")
var option4 = document.getElementById("inputOption4")
var answer  = document.getElementById("answer")
var subject = document.getElementById("subject")

var answerValue = document.getElementById("answerValue")

function checkRequirements()
{
    if (inputTitle.value=='')
    {
            alert("Please provide value for Question Title")
    }
    else if (option1.value=='')
    {
        alert("Please provide value for Option 1")
    }
    else if (option2.value == '') 
    {
        alert("Please provide value for Option 2")
    }
    else if (option3.value == '') 
    {
        alert("Please provide value for Option 3")
    }
    else if (option4.value == '') 
    {
        alert("Please provide value for Option 4")
    }
    else if (answer.value == '')
    {
        alert("Please select Correct Answer")
    }
    else if (subject.value == '')
    {
        alert("Please select Subject")
    }
    else
    {
        console.log(answer.value)
        if (answer.value == '1')
        {
            answerValue.value = option1.value
        }
        else if (answer.value == '2')
        {
            answerValue.value = option2.value
        }
        else if (answer.value == '3')
        {
            answerValue.value = option3.value
        }
        else if (answer.value == '4')
        {
            answerValue.value = option4.value
        }

        console.log("corec answer", answerValue.value)
        document.getElementById("AddQuestion").click()
    }
}

var btn = document.getElementById("btn-js");
// add event listener for the button, for action "click"
btn.addEventListener("click", checkRequirements);