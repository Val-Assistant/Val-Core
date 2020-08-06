import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
    print(audio)
    tts = gTTS(audio, lang='pt-br')
    tts.save(f'hello1.mp3')
    playsound(f'hello1.mp3')
    os.remove('hello1.mp3')

with open('nome.csv') as credenciais_google:
    credenciais_google = credenciais_google.read()

def ouve_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))