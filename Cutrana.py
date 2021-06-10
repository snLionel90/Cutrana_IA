import os
import webbrowser
import speech_recognition as sr
import pywhatkit
import urllib.request
import json
import datetime
import pyttsx3


__Author__ = "snlionel90"

reg = sr.Recognizer() 

while True:
    with sr.Microphone() as source:
        print('Hola,'+__Author__+ 'soy Cutrana, en que pueedo ayudarle?: ')
        audio = reg.listen(source)
 
        try:
            order = reg.recognize_google(audio)
            print('Has dicho: {}'.format(order))
            print(order)

            #bloque de condiciones al hablar por el micro
            if "Google" in order:
                print("Abriendo Google")
                webbrowser.open('https://google.es')
                
            if "Amazon" in order:
                webbrowser.open('https://amazon.es')

            if "noticias" in order:
                webbrowser.open('https://20minutos.es')

            if "buscar en la wiki" in order:
                wikipedia.set_lang("es")
                info = wikipedia.summary(order, 1)
                print(info)

            if "que tal" in order:
                print("Bien y tu?")

            if "A" in order:
                print("lUL")

            if "ponme musica" in order:
                #path = "C:/Program Files (x86)/Windows Media Player/"
                #os.chdir(path)
                os.system("wmplayer.exe")
                print("aaaaaa")

            if "hasta Luego" in order:
                print("hasta luego" +__Author__)

        except:
            print('No entendel, ¿me lo puedes repetir por favor?')
