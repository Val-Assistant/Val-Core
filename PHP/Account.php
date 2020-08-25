<?php
?>
<html>
    <head>
        <meta charset='utf-8'>
        <link rel="stylesheet" href="reset.css">
        <link rel="stylesheet" href="Account.css">
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap" rel="stylesheet">
    </head>
    <header>
        <img class="head" src="https://github.com/Val-Assistant/Val-Core/blob/master/Front-End/pic/20200805_142610.jpg?raw=true" href="home.html">
        <li><a href = "https://github.com/caue-alves/Assitente-Pessoal">Repositório no GitHub</a></li>
        <li><a href = "home.html">Home</a></li>
        <li><a href = "Main.php">Assitente</a></li>
        <li><a href="sign-in.php">Conta</a></li>
        <script src="Main.js"></script>
    </header>
    <body>
        <main>
        <h1 class=title>Criar Conta Val</h1>
            <div class = img>
                <img class="ft-generica" src=https://img.r7.com/images/foto-do-perfil-12072018154519044>
            </div>
            <form action="final.php" method=get>
                <div id="nome">
                    <input type=text class="nome" name = nome placeholder="Digite Aqui seu nome"><br>
                </div>
                <div id = gmail>
                    <input type=text class="gmail" name = gmail placeholder="Digite aqui seu email"><br>
                </div>
                <div id=senha>
                    <input type=text class="senha" name = senha placeholder="Digite sua senha"><br>
                </div>
                <div class=button>
                    <input type=submit id=but>
                </div>
            </form>
        </main>
    </body>
</html>
