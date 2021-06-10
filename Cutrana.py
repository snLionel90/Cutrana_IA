import os
import webbrowser
import speech_recognition as sr
import pywhatkit
import urllib.request
import json
import datetime
import pyttsx3

__Author__ = "snlionel90"
engine = pyttsx3.init()
reg = sr.Recognizer() 

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

while True:
    with sr.Microphone() as source:
        talk('Hola,'+__Author__+ 'soy Cutrana, en que pueedo ayudarle?: ')
        audio = reg.listen(source)
 
        try:
            order = reg.recognize_google(audio, language='es-ES')
            talk('Has dicho: {}'.format(order))
            talk(order)

            #bloque de condiciones al hablar por el micro
            if "Google" in order:
                talk("Abriendo Google")
                webbrowser.open('https://google.es')
                
            elif "Amazon" in order:
                webbrowser.open('https://amazon.es')

            elif "noticias" in order:
                webbrowser.open('https://20minutos.es')

            elif "buscar en la wiki" in order:
                wikipedia.set_lang("es")
                info = wikipedia.summary(order, 1)
                talk(info)

            elif "que tal" in order:
                talk("Bien y tu?")

            elif "Cuentame un chiste" in order:
                talk("lUL")

            elif "ponme musica" in order:
                #path = "C:/Program Files (x86)/Windows Media Player/"
                #os.chdir(path)
                os.system("wmplayer.exe")
                talk("aaaaaa")

            elif "hasta Luego" in order:
                talk("hasta luego" +__Author__)

            else:
                talk("No se ha entendio nada")
        except:
            talk('No entendel, ¿me lo puedes repetir por favor?')
