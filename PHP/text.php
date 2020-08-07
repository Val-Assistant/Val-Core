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
