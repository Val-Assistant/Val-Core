import json
import audio

def converte_json(dicio):
    try:
        with open('package.json', 'w') as jf:
            json.dump(dicio, jf, indent=4)
            if dicio['str'] != "Que função você gostaria de usar?": audio.cria_audio(dicio['str'])
    except OSError:
        print("erro no carregamento")

def carrega_json(position):
    try:
        with open('input.json', 'r') as jf:
            oarq = json.load(jf)
            return oarq[position]
    except json.decoder.JSONDecodeError:
        print("erro no carregamento")

def inicializa():
    try:
        with open('input.json', 'w') as inj:
            json.dump({"input" : ""}, inj, indent=4)
    except OSError:
        print("erro no carregamento")
