#pip install pipwin
#pip install speechrecognition 
#pip install --upgrade speechrecognition
import webbrowser
import speech_recognition as sr
r = sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente por voz, Cutrana, en que pueedo ayudarle?: ')
        audio = r.listen(source)
 
        try:
            text = r.recognize_google(audio)
            print('Has dicho: {}'.format(text))
            print(text)
            if "Google" in text:
                webbrowser.open('https://google.es')
            if "Amazon" in text:
                webbrowser.open('https://amazon.es')
            if "noticias" in text:
                webbrowser.open('https://20minutos.es')
            if "que tal" in text:
                print("Bien y tu?")
        except:
            print('No entendel, ¿me lo puedes repetir por favor?')