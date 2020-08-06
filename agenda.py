import is_in
import json_conv

def agenda(respost, dia_da_semana):
    print(dia_da_semana)

    if dia_da_semana == "Mon":
       info = {"dia": "Segunda", "1": "Ciências", "1.f": "(Videoaula)", "2": "Português", "2.f": "(Aula Online)",
               "3": "Ensino Religioso", "3.f": "(Aula Online)", "4": "Português", "4.f": "(Videoaula)",
               "5": "Geografia", "5.f": "(Aula Online)", "6": "Ciências", "6.f": "(Aula Online)"}
       print(info["dia"], "\n", info["1"], "\n", info["1.f"], "\n \n", info["2"], "\n", info["2.f"], "\n\n", info["3"],
               "\n", info["3.f"], "\n \n", info["4"], "\n", info["4.f"], "\n \n", info["5"], "\n", info["5.f"], "\n \n",
               info["6"], "\n", info["6.f"], "\n \n")

    if dia_da_semana == "Tue":
        info = {"dia": "Terça", "1": "Redação", "1.f": "(Aula Online)", "2": "Matemática", "2.f": "(Aula Online)",
                    "3": "Português", "3.f": "(Aula Online)", "4": "Ciências", "4.f": "(Aula Online)", "5": "Matemática",
                    "5.f": "(Aula Online)", "6": "Inglês", "6.f": "(Videoaula)"}
        print(info["dia"], "\n", info["1"], "\n", info["1.f"], "\n \n", info["2"], "\n", info["2.f"], "\n\n", info["3"],
                  "\n", info["3.f"], "\n \n", info["4"], "\n", info["4.f"], "\n \n", info["5"], "\n", info["5.f"], "\n \n",
                  info["6"], "\n", info["6.f"], "\n \n")

    if dia_da_semana == "Wed":
         info = {"dia": "Quarta", "1": "Ed. Física", "1.f": "(Aula Online)", "2": "História", "2.f": "(Videoaula)",
                    "3": "Ciências", "3.f": "(Aula Online)", "4": "Redação", "4.f": "(Aula Online)", "5": "Português",
                    "5.f": "(Videoaula)", "6": "História", "6.f": "(Aula Online)"}
         print(info["dia"], "\n", info["1"], "\n", info["1.f"], "\n \n", info["2"], "\n", info["2.f"], "\n\n", info["3"],
                  "\n", info["3.f"], "\n \n", info["4"], "\n", info["4.f"], "\n \n", info["5"], "\n", info["5.f"], "\n \n",
                  info["6"], "\n", info["6.f"], "\n \n")

    if dia_da_semana == "Thu":
         info = {"dia": "Quinta", "1": "Inglês", "1.f": "(Aula Online)", "2": "Geografia", "2.f": "(Videoaula)",
                    "3": "Matemática", "3.f": "(Aula Online)", "4": "Matemática", "4.f": "(Videoaula)", "5": "História",
                    "5.f": "(Aula Online)", "6": "Português", "6.f": "(Aula Online)"}
         print(info["dia"], "\n", info["1"], "\n", info["1.f"], "\n \n", info["2"], "\n", info["2.f"], "\n\n", info["3"],
                  "\n", info["3.f"], "\n \n", info["4"], "\n", info["4.f"], "\n \n", info["5"], "\n", info["5.f"], "\n \n",
                  info["6"], "\n", info["6.f"], "\n \n")

    if dia_da_semana == "Fri":
       info = {"dia": "Sexta", "1": "Matemática", "1.f": "(Videoaula)", "2": "Rac. Lógico", "2.f": "(Aula Online)",
                    "3": "Geografia", "3.f": "(Aula Online)", "4": "Artes", "4.f": "(Aula Online)", "5": "Ed. Física",
                    "5.f": "(Videoaula)", "6": "Matemática", "6.f": "(Aula Online)"}
       print(info["dia"], "\n", info["1"], "\n", info["1.f"], "\n \n", info["2"], "\n", info["2.f"], "\n\n", info["3"],
                  "\n", info["3.f"], "\n \n", info["4"], "\n", info["4.f"], "\n \n", info["5"], "\n", info["5.f"], "\n \n",
                  info["6"], "\n", info["6.f"], "\n \n")



