<?php

require_once('Json_file.php');

try {
    $Json = new Json_file('C:\Users\evers\PycharmProjects\Assitente\package.json');
    $Json_val = $Json->GetValor('str');
} catch (Exception $Json) {
    echo "<br>Erro no carregamento do JSON<br>";
}

?>
<html>
    <head>
        <link rel="stylesheet" href="../Front-End/CSS/reset.css">
        <link rel="stylesheet" href="../Front-End/CSS/style.css">
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap" rel="stylesheet">
        <meta charset="UTF-8">
    </head>
    <header>
        <img class="head" src="https://github.com/Val-Assistant/Val-Core/blob/master/Front-End/pic/20200805_142610.jpg?raw=true" href="home.html">
        <li><a href = "https://github.com/caue-alves/Assitente-Pessoal">Repositório no GitHub</a></li>
        <li><a href = "../Front-End/HTML/home.html">Home</a></li>
        <li><a href = "Main.php">Assitente</a></li>
        <li><a href="sign-in.php">Conta</a></li>
        <li class="datetime">Hora</li>
        <li class = 'minutozz'>minutos</li>
        <script src="../Front-End/js/Main.js"></script>
        <script src="../Front-End/js/date.js"></script>
    </header>
    <main>
        <div class = "all-content" style="overflow-y: auto;">
            <nav class = msg id="msg">
                <?php echo "<p id=titulo >Val: $Json_val</p>"?>
                <div class="return">  
                </div>
            </nav>
            <div class = "div">
                <iframe name="input" style="display:none;"></iframe>
                <form action="text.php" method=get target="input">
                    <input type=text name=nome id="name" placeholder="Digite aqui seu comando:"><br>
                    <input type=submit id="but" onclick="capturar()">
                </form>
            </div>
        </div>
    </main>
</html>