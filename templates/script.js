$( "#contact_form" ).submit(function( event ) {
    var text = $('#contact_form').find('input[name="name"]').val();
    $("#contact_form").addClass("shrink");
    $(".container").addClass("bgchange");
    $(".thanks").addClass("reveal");
    $("body").addClass("invert");
    $( ".thanks" ).append( "<span>" + text + "</span>" );
    event.preventDefault();
    
  });
  
  