"""

MIT License

Copyright (c) 2020 Val

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

import random, re, audio, json_conv, web
import is_in
from datetime import datetime
src = open('nome.csv', mode='a')
sr = open('nome.csv', mode='r')
content = sr.readline()

if content == "":
    nome = input("Qual é o seu nome? ")
    src.write(nome)

src = open('nome.csv', mode='r')
content = src.readline()
nome = content
src.flush()
src.close()


possibilidades = [f"Olá {nome}, como vai?",
    f"Olá {nome}, o dia está lindo hoje não é mesmo?",
    f"Bom dia {nome}, tudo bem?",
    f"Olá {nome}, que dia lindo para fazer uns uptades em mim hehe",
    "Iae brô, tudo na paz?"
]
audio.cria_audio(possibilidades[random.randrange(0, len(possibilidades))])
resposta = ""

dias_da_semana = ["Mon", "Tue", "Wed", "Thu", "Fri" ]
find = ["Sun", "Sat"]
contador = 0
awnser = ""

while contador == 0:
    json_conv.inicializa()
    hoje1 = datetime.today()
    hoje = hoje1.strftime("%a/%d/%m/%Y %H:%M")
    dia_da_semana = hoje1.strftime("%a")
    json_conv.converte_json({'str': "Que função você gostaria de usar?"})
    hoje1 = hoje[15 : ]
    respost = json_conv.carrega_json("input")

    if dia_da_semana in dias_da_semana:
        import agenda
        if is_in.str("agenda", respost):
            agenda.agenda(respost, dia_da_semana)
    elif is_in.str(dia_da_semana, find):
        print(f"{resposta} não tem aula, é fim de semana!")
    else:
        print("Dia não encontrado")

    if is_in.str("PIADA", respost) or is_in.str("PIADAS", respost):
        import piada
        piada.piada()

    elif is_in.str("CALCULADORA", respost) or is_in.str("CALCULAR", respost) or not is_in.str("CALCULADORA", respost) or not is_in.str("CALCULAR", respost):
        import conv
        conv.calc(respost)

    elif is_in.str("IMC", respost):
        import imc
        imc.f(respost)

    elif is_in.str("ALARME", respost):
        padrao = "[0-9]{2}[:][0-9]{2}"
        search = re.findall(padrao, respost)
        if search != "":
            if search == []:
                audio.cria_audio("Bem vindo à função de alarme diga para que horas você deseja \ndefinir")
                awnser = input()
                print(awnser)
            else:
                awnser = search[0]

    if hoje1 == awnser:
        contador = 1
        print("\nAlerta, alarme terminado!")
        awnser = ""

    if is_in.str("FECHAR",respost):
        break

    if is_in.str("CONVERSOR",respost):
        import conversor
        conversor.conve()
    if is_in.str("RENOMEAR", respost):
        import renom
        renom.renomear(respost)

    if is_in.str("NOTÍCIA", respost):
        web.scrapping()

    if is_in.str("TOQUE", respost):
        web.playlists(respost)

    if is_in.str("PREVISÃO", respost) and is_in.str("TEMPO", respost):
        web.previsao_do_tempo()
        contador = 0

    if is_in.str("ADICIONE", respost):
        import grafico
        grafico.adiciona_nota()

    if is_in.str("GRÁFICO", respost):
        import grafico
        grafico.grafico()

    if is_in.str("CASOS DE COVID", respost):
        web.covid_cases()

    if is_in.str("BUSQUE", respost) and not is_in.str("DICIONÁRIO", respost) and not is_in.str("WIKI", respost) and not is_in.str("STACK", respost) and not is_in.str("YOUTUBE", respost):
        web.google(respost)

    if is_in.str("DICIONÁRIO", respost):
        web.dicio(respost)

    if is_in.str("WIKIPEDIA", respost):
        web.wiki(respost)

    if is_in.str("CRIE", respost) and is_in.str("PASTA", respost):
        import os_file
        os_file.mkd(respost)

    if is_in.str("STACK", respost) and is_in.str("OVERFLOW", respost):
        web.stack(respost)

    if is_in.str("YOUTUBE", respost):
        web.youtube(respost)





