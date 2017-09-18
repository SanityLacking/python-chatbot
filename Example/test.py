# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from translate import Translator
from korean import Noun
from Example.data_formatter import Data_Formatter

from build.exe.win-amd64-3.5.chatterbot.trainers import ChatterBotCorpusTrainer

# Chatbot name
chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

def train():
    
# This code tells the Chatbot that we are going to use corpus data in English.
chatterbot.train('chatterbot.corpus.english')
# this is the location of the corpus data.
chatterbot.train(
    "chatterbot.corpus.english.greetings"
  
)

def search(entered_input):
      #haystack = entered_input
      
     print(entered_input)
      haystack = entered_input     

      response = bot.get_response(haystack)
      print(response)
      return(response)