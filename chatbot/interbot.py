import time

#for creating a chatbot
from chatterbot import ChatBot

#for creating a trainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot is created and this cbot will be used later in the program to train and stuff
cbot1 = ChatBot('mybot')

#Create 1st trainer for the chatbot which will train the chatbot1
trainer1 = ChatterBotCorpusTrainer(cbot1)

#chatbot 2
cbot2 = ChatBot('mybot2')

#Create 2nd trainer for the chatbot which will train the chatbot2
trainer2 = ChatterBotCorpusTrainer(cbot2)


#Now train the chatbots using this english corpus
trainer1.train("chatterbot.corpus.english")
trainer2.train("chatterbot.corpus.english")

def responding1(message):
    # Get a response to an input statement
    response1=cbot1.get_response(message)
    print("Bot1:",response1)
    time.sleep(0.1)
    responding2(response1)


def responding2(message):
    # Get a response to an input statement
    response2=cbot2.get_response(message)
    print("Bot2:",response2)
    time.sleep(0.1)
    responding1(response2)


responding1("Hi, How are you!!")


