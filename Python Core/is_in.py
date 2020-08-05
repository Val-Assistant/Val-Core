def str(frase, str):
    try:
        if frase.upper() in str.upper():
            return True
        else:
            return False
    except AttributeError:
        print("Erro com a classe dos arquivos especificados")

def array(frase, array):
    try:
        for i in array:
            i.split()
            if i.upper() == frase:
                return True
                break
        return False
    except AttributeError:
        print("Erro com a classe dos arquivos especificados")
