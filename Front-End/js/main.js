var capturando = "";
var nova_div = document.createElement("div");
function capturar() {
    var mbox = document.querySelector(".return");
    var capturando = document.getElementById('name');
    var textCap = capturando.textContent;
    var msg = document.createElement("p");
    msg.textContent = "Você: " + textCap;
    mbox.appendChild(nova_div);
    var ref = document.querySelector("nav div div");
    ref.appendChild(msg);
}
