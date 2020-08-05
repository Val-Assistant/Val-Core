<?php
    require_once('Json_File.php');
    try {
        $input = $_GET['nome'];
    } catch(Exception $input) {
        echo "Falha na captura do input";
    }

    try {
        $inputClass = new Json_file('C:\Users\evers\PycharmProjects\Assitente\input.json');
        $inputClass->CreateValue($input);
    } catch (Exception $inputClass) {
        echo "Falha na criação do arquivo JSON";
    }

?>
<html>
    <head>
        <meta charset = "UTF-8">
        <link rel="stylesheet" href="reset.css">
        <link rel="stylesheet" href="text.css">
        <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap" rel="stylesheet">
    </head>
    <main>
        <?php echo "<p>Você respondeu $input<p>"?>
        <ul>
            <li><a href=http://localhost/Main.php>Clique aqui para voltar à tela inicial</a></li>
    </main>