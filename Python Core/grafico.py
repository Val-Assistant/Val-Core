import matplotlib.pyplot as plt
import audio
w = open('quantas_vezes.txt', 'a')
notas = []
r = open('quantas_vezes.txt', 'r')
for line in r:
    notas.append(line)
yum = open('y.txt', mode='r')
ydo = open('y.txt', mode='a')
y = []
for linha in yum:
    y.append(int(linha))
x = notas


def grafico():
    plt.plot(x, y, marker='o')
    plt.title('Notas de Mat')
    plt.xlabel("Prova")
    plt.ylabel("Notas")
    plt.show()

def adiciona_nota():
    print("Olá de que matéria você gostaria de inserir sua nota?")
    inp = ""
    print("Qual é a nota?")
    inpt = ""
    w.write(f"{inp}\n")
    ydo.write(f"{inpt}\n")
    w.flush()
    ydo.flush()




