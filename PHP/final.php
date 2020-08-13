<?php
$nome = $_GET['nome'];
$email = $_GET['gmail'];
$senha = $_GET['senha'];

echo "$nome, $email, $senha";

$array = [
    "nome" => $nome,
    "senha" => $senha,
    "email" => $email
];

$array_formatado = json_encode($array);
$arqj = fopen('C:\Users\evers\PycharmProjects\Assitente\ac.json', 'w');
fwrite($arqj, $array_formatado);
?>