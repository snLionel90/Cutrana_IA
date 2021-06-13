import speech_recognition as sr
import pyttsx3
import pywhatkit
import requests, json, sys,os, datetime
import webbrowser
import time
import subprocess

__Author__ = "snlionel90"

print('Opening....')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def spk(txt):
    engine.say(txt)
    engine.runAndWait()


def comands():
    reg = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        sound=reg.listen(source)

        try:
            status=reg.recognize_google(sound,key = None,language='en-US',show_all=False)
            print(f"user said:{status}\n")

        except Exception as e:
            spk("Lo siento, pero no e entendido la petición, repitemela por favor")
            print("Lo siento, pero no e entendido la petición, repitemela por favor")
            return "None"
        return status

if __name__=='__main__':

    while True:
        spk("Hola, ese ene lionel noventa. soy Cutrana, el asistente por voz, en que puedo ayudarle?")
        print("Hola snLionel90,soy Cutrana, el asistente por voz, en que puedo ayudarle?")
        status = comands().lower()
        if status ==0:
            continue

        if "open news " in status or "ultima hora" in status:
            webbrowser.open('https://20minutos.es')
            spk('Abruiendo el panel de noticias')
            time.sleep(5)

        elif "open google" in status:
            webbrowser.open_new_tab ('https://google.es')
            spk('Abriendo el navegador de internet, con google')
            time.sleep(6)
        
        elif "open job" in status:
            webbrowser.open_new_tab ('https://www.linkedin.com/?trk=public_jobs_nav-header-logo')
            spk('abriendo linkedin')
            time.sleep(4)

        elif "log off" in status or "apagar" in status:
            spk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            time.sleep(5)
    
time.sleep(3)



