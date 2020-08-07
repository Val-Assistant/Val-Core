var capturando = "";
var msg = ""
var nova_div = document.createElement("div")

function capturar () {
    var mbox = document.querySelector(".return");
    capturando = document.getElementById('name').value;
    msg = document.createElement("p");
    msg.textContent = "Você: " + capturando;
    mbox.appendChild(nova_div);
    ref = document.querySelector("nav div div");
    ref.appendChild(msg);
}

