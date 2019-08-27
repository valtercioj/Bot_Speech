from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# speech recognition
import speech_recognition as sr

# speech systhesis
import pyttsx3

bot = ChatBot('Jarvis')

chats = ['oi', 'ola', 'tudo bom?', 'tudo e voce?', 'estou bem obrigado.']

bot.set_trainer(ListTrainer) # define o metodo de treinamento
bot.train(chats) # define a lista de conversas

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambien_noise(s) #se adaptar ao ruido 

    while True:
        audrio = r.listen(s) # escutar

        speech = r.recognize_google(audio, language='pt') # fala

        print(bot.get_response(speech))



