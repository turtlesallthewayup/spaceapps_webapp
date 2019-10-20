$(document).ready(function () {
    var imageCapture;
var images = [];

function onGetUserMediaButtonClick() {
  navigator.mediaDevices.getUserMedia({video: true})
  .then(mediaStream => {
    document.querySelector('video').srcObject = mediaStream;

    const track = mediaStream.getVideoTracks()[0];
    imageCapture = new ImageCapture(track);
  })
  .catch(error => ChromeSamples.log(error));
}

function onGrabFrameButtonClick() {
  
  // imageCapture.takePhoto()
  // .then(blob => createImageBitmap(blob))
  // .then(imageBitmap => {
  //   const canvas = document.querySelector('#takePhotoCanvas');
  //   drawCanvas(canvas, imageBitmap);
  // })
  // .catch(error => console.log(error));
  
  
  
  imageCapture.grabFrame()
  .then(imageBitmap => {
    images.push(drawCanvas(imageBitmap));
  }).catch(error => console.error(error));
  // .catch(error => ChromeSamples.log(error));
}


/* Utils */

function drawCanvas(img) {
  canvas = document.createElement('canvas');
  console.log(img);
  canvas.width = 350;
  canvas.height = 350;
  

  let ratio  = Math.min(canvas.width / img.width, canvas.height / img.height);
  let x = (canvas.width - img.width * ratio) / 2;
  let y = (canvas.height - img.height * ratio) / 2;
  canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
  canvas.getContext('2d').drawImage(img, 0, 0, img.width, img.height,
      x, y, img.width * ratio, img.height * ratio);
  return canvas.toDataURL();
}



function handleError(error) {
  console.error('navigator.getUserMedia error: ', error);
}
const constraints = {video: true};



(function() {
  const video = document.querySelector('#basic video');
  const captureVideoButton = document.querySelector('#basic .capture-button');
  const x = null
  const fd = new FormData()
  
  function handleSuccess(stream) {
    
    localMediaStream = stream;
    video.srcObject = stream;
    
  }

 function stopEventStreming(label) {
    
    // var list_tmp = []
    
    // $(images).each(function(i, obj){
      
      
    //   console.log(obj);
    //   console.log(typeof(obj));

    //   // console.log(obj.image.toString('base64'));

      
    //   // list_tmp.push(obj.image.toString('base64'));
      
    // });
    
    // images = list_tmp
    
    console.log(images)
  
    //video.pause();
    // localMediaStream.stop();
    console.log('STOP COMPLETE');
    
     $.ajax({
            url: $("#receive_blob_url").val(),
            data: {
                images:images,
                label:label,
            },
            dataType: 'json',
            method:"POST",
            success: function(data) {
                if (data) {
                    console.log(data.message);
                    $('#cash_in').text('R$ ' + data.cash)
                }
            }
        });
  }
  
  $(".capture-button").on('click', function() {
    
    console.log('CAPTURE BUTTON')
    var label = $("#label").val()
    var time = 5;
    var x = setInterval(function(){
      onGrabFrameButtonClick()   
      if (time < 0) {
        clearInterval(x);
        stopEventStreming(label);
      }
      time = time-1;
    }, 500);
    
  });


})();

(function() {
  onGetUserMediaButtonClick()
  const captureVideoButton = document.querySelector('#screenshot .capture-button');
  const screenshotButton = document.querySelector('#screenshot-button');
  const img = document.querySelector('#screenshot img');
  const video = document.querySelector('#screenshot video');

  const canvas = document.createElement('canvas');

  $(".capture-button").on('click', function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  });

  

  function handleSuccess(stream) {
    console.log("stream:",stream)
    screenshotButton.disabled = false;
    video.srcObject = stream;
  }
})();

(function() {

  $(".capture-button").on('click', function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  });

  function handleSuccess(stream) {
    video.srcObject = stream;
  }
})();

});