from os import makedirs
import audio

def mkd(respost):
    respost1 = respost.upper()
    index = respost1.find("PASTA")
    print(index)
    index += 6
    dir = respost[index: ]
    audio.cria_audio(f"CRIANDO A PASTA {dir}...")
    makedirs(dir)
