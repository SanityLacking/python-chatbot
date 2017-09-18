# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from translate import Translator
from korean import Noun
from Example.data_formatter import Data_Formatter

formatter = Data_Formatter('Example/Eduhouse.csv')

responsek=' '
# Create a new instance of a ChatBot
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'Can you please make your question more specific?'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

def train():
      
      # Train the chat bot with a few responses
      bot.train(formatter.get_training_array()[2])
      formatter.get_training_array()[1]

#while True:
# Get a response for some unexpected input
#response = bot.get_response('How do I make an omelette?')
 #     entered_input = input("Please enter your text: ")
def search(entered_input):
      #haystack = entered_input
      translator= Translator(to_lang="en")
      entered_input = translator.translate(entered_input)
      print(entered_input)
      entered_input = entered_input.lower()
      haystack = entered_input

     
      response = bot.get_response(haystack)
 #     response=str(responsek)+'\n\n'+str(response2)
  #    print(response2)
  #    print(responsek)
      print(response)
      return(response)

#response = bot.get_response(entered_input)
#print(response)
