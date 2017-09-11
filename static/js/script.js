$(document).ready(function(){
    
     $("#submitBtn").keypress(function(event) {
        if (event.which == 13) {
            event.preventDefault();
            search($("#inputText").val());
            $( "#results" ).focus();
        }
    });
})

function submitText(inputText){
    //var input = {[]}
}