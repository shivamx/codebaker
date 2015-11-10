$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

   
  $('#button1').click(function(){ 
    alert($('#combo :selected').text());
  });


});