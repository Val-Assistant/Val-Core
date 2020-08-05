<?php

Class Json_file 
{

    private string $path;

    function __construct($path){
        $this->path = $path;
    }

    public function GetPath()
    {
        return $this->path;
    }

    public function GetValor($po)
    {
        $file = file_get_contents($this->path, 'r');
        $json = json_decode($file);
        return $json->$po;
    }

    public function CreateValue($input)
    {
        $dicio = ["input" => $input];
        $dicio_json = json_encode($dicio);
        $arqj = fopen('C:\Users\evers\PycharmProjects\Assitente\input.json', 'w');
        fwrite($arqj, $dicio_json);
        
    }
}

