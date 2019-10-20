
function execCam() {
    var fiveMinutes = 5, display = document.querySelector('#stop-button');

$(document).ready(function(){
    $('#next').hide();
    $("#again").hide();
   $('.capture-button').on('click', function (e) {
       console.log("log capture click");
       startTimer(fiveMinutes, display);
        $('.videostream').show();
        $('.capture-button').hide();
        $('#stop-button').show();
        $('#next').hide();  
    });  
   $( ".item-menu" ).removeClass( "active" );
   $( ".menu-treino" ).addClass( "active" );
   $('#stop-button').hide();
      
  
});

function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    let interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        
        display.textContent = minutes + ":" + seconds;
        console.log(seconds);

        if (seconds == 0) {
            $("#stop-button").hide();
            $("#again").show();
            $('#next').show();
            clearInterval(interval);
            
        }
      
        if (--timer < 0) {
            timer = duration;
            return;
        }
        
    
    }, 1000);
}
}

