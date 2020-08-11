import is_in
import audio

def conve():
    print("Bem vindo à função de conversor, o que você deseja converter?" )
    C1 = ""
    if "TEMPERATURA" in C1.upper():
        qual = input("Qual é a primeira medida? ")
        qual2 = input("Qual é a segunda medida? ")
        qual.split()
        if is_in.str("CELSIUS", qual):
            first = "CELSIUS"
        elif is_in.str("CELSIUS", qual):
            sec = "CELSIUS"

        if is_in.str("FARENHEIT", qual):
            first = "FARENHEIT"

        elif is_in.str("FARENHEIT", qual2):
            sec = "FARENHEIT"

        if is_in.str("KELVIN", qual):
            first = "KELVIN"
        elif is_in.str("KELVIN", qual2):
            sec = "KELVIN"

        if first == "CELSIUS" and sec == "FARENHEIT":
            C = float(input("Qual é a medida em celsius? "))
            audio.cria_audio(f"{(C * 9 / 5) + 32} Fº")
        elif first == "FARENHEIT" and sec == "CELSIUS":
            C = float(input("Qual é a medida em Farenheit?" ))
            audio.cria_audio(f"{(C - 32) * 5 / 9}°C")
        elif first == "CELSIUS" and sec == "KELVIN":
            C = float(input("Qual a medida em celsius? "))
            audio.cria_audio(f"{C + 273,15}K")
        elif first == "KELVIN" and sec == "CELSIUS":
            C = float(input("Qual a medida em kelvin? "))
            audio.cria_audio(f"{C - 273,15}°C")
        elif first == "KELVIN" and sec == "":
            C = float(input("Qual a medida em kelvin? "))
            audio.cria_audio(f"{C - 273,15}°C")
        elif first == "FARENHEIT" and sec == "KELVIN":
            C = float(input("Qual a medida em Farenheit? "))
            audio.cria_audio(f"{(C - 32) * 5/9 + 273,15}K")
