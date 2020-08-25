<?php
?>
<html>
    <head>
        <link rel="stylesheet" href="sign-in.css">
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap" rel="stylesheet">
    </head>
    <header>
        <img class="head" src="https://github.com/Val-Assistant/Val-Core/blob/master/Front-End/pic/20200805_142610.jpg?raw=true" href="home.html">
        <li><a href = "https://github.com/caue-alves/Assitente-Pessoal">Repositório no GitHub</a></li>
        <li><a href = "home.html">Home</a></li>
        <li><a href = "Main.php">Assitente</a></li>
        <li><a href="Account.php">Conta</a></li>
        <script src="Main.js"></script>
    </header>
    <body>
        <main>
            <h1 class = title>Logon</h1>
            <div class = img>
                <img class="ft-generica" src=https://img.r7.com/images/foto-do-perfil-12072018154519044>
            </div>
            <form action="final-logon.php" method=get>
            <div id = gmail>
                    <input type=text class="gmail" name = gmail placeholder="Digite aqui seu nome ou email"><br>
                </div>
                <div id=senha>
                    <input type=text class="senha" name = senha placeholder="Digite sua senha"><br>
                </div>
                    <p>Ainda não tem conta? <a href="Account.php">Crie uma</a></p>
                <div class=button>
                    <input type=submit id=but>
                </div>
            </form>
        </main>
    </body>
</html>
