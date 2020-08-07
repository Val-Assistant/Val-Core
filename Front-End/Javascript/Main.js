var capturando = "";
var msg = ""

function capturar () {
    var mbox = document.querySelector(".return");
    capturando = document.getElementById('name').value;
    msg = document.createElement("p");
    msg.textContent = capturando;
    console.log(msg)
    mbox.appendChild(msg);
}

