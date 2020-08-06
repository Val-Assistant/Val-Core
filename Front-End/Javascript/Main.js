let box = document.querySelectorAll('.msg')

var capturando = "";

function capturar () {
    capturando = document.getElementById('valor').value;
    array = '{ "anterior" : ' + capturando + '}'
    var obj = JSON.parse(array)
}

