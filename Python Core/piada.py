import random
import json_conv
def piada():
    piadas = ["O que o pagodeiro foi fazer na igreja?\nfoi cantar pá-god",
              "Por que o Napoleão sempre era chamada para festas?\nPor que ele era bom-na-party",
              "Você conhece a piada do ponêi?\nPô nem eu", "Qual é o rei dos queijos\n o reiqueijão",
              "O que o pato falou pra pata?\nvem quá", "POr que a velhinha não tem relógio\nPor que ela era sem hora",
              "O que a xuxa foi fazer no bar?\nfoi beber ca sasha"]
    json_conv.converte_json({"str" : f"{piadas[round(random.randrange(0, len(piadas)))]}"})