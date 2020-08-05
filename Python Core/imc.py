import re
import audio
import json_conv
from time import sleep

def f(respost):
    padrao1 = "[0-9]{2,3} [1-3][.][0-9]{2}"
    search = re.findall(padrao1[: 10], respost)
    search2 = re.findall(padrao1[11:], respost)
    if search != [] and search2 != []:
        peso = int(search[0])
        altura = float(search2[0])
    else:
        json_conv.converte_json({'str' : "Bem vindo à função de IMC, para começarmos me diga seu peso:"})
        sleep(3)
        peso = float(json_conv.carrega_json('input'))
        json_conv.converte_json({'str' : "Agora me diga sua altura"})
        sleep(4)
        altura = float(json_conv.carrega_json('input'))
    resultado = round(peso / (altura * altura))
    audio.cria_audio(f"O seu IMC é de {resultado}")