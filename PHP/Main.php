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
        <link rel="stylesheet" href="reset.css">
        <link rel="stylesheet" href="style.css">
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap" rel="stylesheet">
        <meta charset="UTF-8">
    </head>
    <header>
        <img class="head" src="https://github.com/caue-alves/Val-Assistente-Pessoal/raw/master/Front-End/pic/20200805_142610.jpg?raw=true" href="home.html">
        <li><a href = "https://github.com/caue-alves/Assitente-Pessoal">Repositório no GitHub</a></li>
        <li><a href = "home.html">Home</a></li>
        <li><a href = "Main.php">Assitente</a></li>
        <script src="Main.js"></script>
    </header>
    <main>
        <div class = "all-content">
            <nav class = msg>
                <?php echo "<p id=titulo >$Json_val</p>"?>
            </nav>
            <div class = "div">
                <form action="text.php" method=get>
                    <input type=text name=nome id="name" placeholder="Digite aqui seu comando:"><br>
                    <input type=submit id="but" onclick="capturar()">
                </form>
            </div>
        </div>
    </main>
</html>