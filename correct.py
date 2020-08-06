import nltk

with open('artigos.txt', 'r', encoding='utf-8') as corpus:
    data = corpus.read()

def corrige():
    palavras_final = []
    palavras_separadas = nltk.tokenize.word_tokenize(data)
    for palavra in palavras_separadas:
        if palavra.isalpha():
            palavras_final.append(palavra)
    palavras_final_true = [palavra.lower() for palavra in palavras_final]
    return palavras_final_true

palavras_separadas = corrige()

def separa(palavra):
    fatias =[]
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    return avalia(fatias)

def avalia(fatias):
    retorno = []
    letras = "abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç"
    for E, D in fatias:
        for letra in letras:
            if E + letra + D in palavras_separadas:
                retorno.append(E + letra + D)
    return retorno

def separa_true(palavra):
    palavra = separa(palavra)
    return palavra[0]

