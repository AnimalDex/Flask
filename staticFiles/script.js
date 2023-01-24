window.setInterval(function () {
  const request = new XMLHttpRequest();
  request.open('POST', '/animal', true);
  request.onload = () => {
    const response = request.responseText;
    document.getElementById('count').innerHTML = response;
  }; 
  request.send();
}, 100);

const play = document.querySelector('.play');
const pause = document.querySelector('.pause');
const playBtn = document.querySelector('.circle__btn');
const wave1 = document.querySelector('.circle__back-1');
const wave2 = document.querySelector('.circle__back-2');

playBtn.addEventListener ('click', function(e) {
  e.preventDefault();
  pause.classList.toggle('visibility');
  play.classList.toggle('visibility');
  playBtn.classList.toggle('shadow');
  animacionCargando();
  cargarImagen();
});

function wait(ms){
  var start = new Date().getTime();
  var end = start;
  while(end < start + ms) {
    end = new Date().getTime();
 }
}

function esperandoResultado() {
  console.log("Esperando 1 s");
  wait(1000);
}

function arreglarBoton() {
  document.querySelector(".load-9").style.display = "none";
  pause.classList.toggle('visibility');
  play.classList.toggle('visibility');
  playBtn.classList.toggle('shadow');
  document.querySelector(".col-sm-12").style.display = "block";
}

function animacionCargando() {
  console.log("Animacion Cargando");
  wave1.classList.toggle('paused');
  wave2.classList.toggle('paused');
  document.querySelector(".load-9").style.display = "block";
}

function cargarImagen() {
  context.drawImage(video, 0, 0, 100, 100);
  canvas.toBlob(upload, "image/jpeg");
}