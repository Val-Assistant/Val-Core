import audio
import re

def renomear(respost):
    arq = open('nome.csv', mode='w')
    index = respost.find(" ")
    new = respost[index + 1 : ]
    arq.write(new)
