from requests import get
from bs4 import BeautifulSoup
import audio
import webbrowser as cr
import json

def scrapping():
    site = get("https://news.google.com/rss?need=pt_br&gl=BR&hl=pt-BR&ceid=BR:pt-419")
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:
        audio.cria_audio(f"{item.title.text}\n")

def playlists(respost):
    index = respost.find("E ")
    musica = respost[index + 1 : ]
    if musica.upper() == 'DIA ESPECIAL':
        cr.open_new_tab('https://open.spotify.com/track/5ovqe99T1FShehFNSs9qgy?si = FwSuYvc_TtSoiDBHOizdsg')
    if musica.upper() == 'MACARENA':
        cr.open_new_tab('https://open.spotify.com/track/4oaj36KzXRgDg4McgcTsZK?si=v-8NEjIKQJS414aeNLhObg')

def previsao_do_tempo():
    site = get('http://api.openweathermap.org/data/2.5/weather?lat=-29.6842&lon=-53.8069&appid=90215b527139cc03551eff4bb45ea00f&units=metric&lang=pt')
    clima = site.json()
    temperatura = clima['main']['temp']
    fell = clima['main']['feels_like']
    descrição = clima['weather'][0]['description']
    audio.cria_audio(f"Temperatura atual: {temperatura} graus, sensação térmica de {fell} graus, situação atual do céu {descrição}")

def covid_cases():
    site = get('https://covid19-brazil-api.now.sh/api/report/v1')
    casos = site.json()
    caso = casos['data'][14]['cases']
    suspeitos = casos['data'][14]['suspects']
    mortes = casos['data'][14]['deaths']
    audio.cria_audio(f"Agora existem: {caso} casos de Covid em seu estado, com {suspeitos} casos suspeitos e {mortes} mortes")

def google(respost):
    index = respost.find("e")
    r = respost[index + 2 : ]
    print(f"buscando por {r}")
    cr.open_new_tab(f"https://www.google.com/search?q={r}")

def dicio(respost):
    respost1 = respost.upper()
    index = respost1.find("RIO")
    termo = respost[index + 3 : ]
    cr.open_new_tab(f"https://www.dicio.com.br/pesquisa.php?q={termo}")
    if termo == -1:
        print("termo não encontrado")

def wiki(respost):
    respost1 = respost.upper()
    index = respost1.find("PEDIA")
    termo = respost[index + 5 :]
    cr.open_new_tab(f'https://pt.wikipedia.org/w/index.php?search={termo}')

def stack(respost):
    respost1 = respost.upper()
    index = respost1.find("FLOW")
    termo = respost[index + 4 : ]
    cr.open_new_tab(f'https://pt.stackoverflow.com/questions/tagged/{termo}')

def youtube(respost):
    r1 = respost.upper()
    index = r1.find("TUBE")
    termo = respost[index + 4 : ]
    cr.open_new_tab(f"https://www.youtube.com/results?search_query={termo}")