import re
import is_in
import audio

def calc(respost):
    if is_in.str("MULTIPLICAÇÃO", respost) or is_in.str("MULTIPLIQUE", respost):
        p = "[0-9]{1,100}"
        s = re.findall(p, respost)
        if len(s) == 2:
            aws2 = int(s[0])
            aws3 = int(s[1])
        else:
            aws2 = int(input("Qual é o multiplicando?"))
            aws3 = int(input("Qual é o multiplicador?"))
        audio.cria_audio(f"Produto {aws2 * aws3}")
    else:
        if is_in.str("DIVISÃO", respost) or is_in.str("DIVIDA", respost):
            p = "[0-9]{1,100}"
            s = re.findall(p, respost)
            if len(s) == 2:
                aws2 = int(s[0])
                aws3 = int(s[1])
            else:
                aws2 = int(input("Qual é o dividendo?"))
                aws3 = int(input("Qual é o divisor?"))
            audio.cria_audio(f"Quociente {aws2 / aws3}")
        else:
            if is_in.str("ADIÇÃO", respost) or is_in.str("ADICIONE", respost):
                p = "[0-9]{1,100}"
                s = re.findall(p, respost)
                if len(s) == 2:
                    aws2 = int(s[0])
                    aws3 = int(s[1])
                else:
                    aws2 = int(input("Qual é a primeira parcela?"))
                    aws3 = int(input("Qual é a segunda parcela?"))
                audio.cria_audio(f"Total {aws2 + aws3}")
            else:
                if is_in.str("SUBTRAÇÃO", respost) or is_in.str("SUBTRAIA", respost):
                    p = "[0-9]{1,100}"
                    s = re.findall(p, respost)
                    if len(s) == 2:
                        aws2 = int(s[0])
                        aws3 = int(s[1])
                    else:
                        aws2 = int(input("Qual é o minuendo?"))
                        aws3 = int(input("Qual é subtraendo?"))
                    audio.cria_audio(f"Diferença {aws2 - aws3}")
                else:
                    if is_in.str("POTENCIAÇÃO", respost) or is_in.str("POTÊNCIA", respost):
                        aws2 = int(input("Qual é a base?"))
                        aws3 = int(input("Qual é o expoente?"))

                        audio.cria_audio(f"Potência {aws2 ** aws3}")
