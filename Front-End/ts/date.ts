var date = new Date()
var day = date.getDate();
var month = date.getMonth();
var year = date.getFullYear();
var dateFormatted = day +'/'+ (month++) +'/'+ year;

var dateInDom = document.querySelector('.datetime');
var minutos = date.getMinutes();
var horas = date.getHours();

if(String(minutos).length == 1) {
    minutos = 0 + date.getMinutes();
}

var exactDate =  horas + ":" + minutos;
dateInDom.textContent = dateFormatted;

var minutes = document.querySelector('.minutozz');
minutes.textContent = exactDate;