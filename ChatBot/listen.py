import speech_recognition as sr
from time import sleep


def ouvir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('falar')
        audio = r.listen(source)
        print('ok')
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        print('Erro durante reconhecimento de voz. Verifique a conexão com a internet ou a qualidade e clareza do áudio recebido e tente')
    
