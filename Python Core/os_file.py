from os import makedirs
import audio

def mkd(respost):
    respost1 = respost.upper()
    index = respost1.find("PASTA")
    index += 6
    dir = respost[index: ]
    makedirs(dir)
    audio.cria_audio(f"CRIANDO A PASTA {dir}...")

