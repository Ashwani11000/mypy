#for creating a chatbot
from chatterbot import ChatBot

#for creating a trainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot is created and this cbot will be used later in the program to train and stuff
cbot = ChatBot('mybot')

#Create a trainer for the chatbot which will train the chatbot
trainer = ChatterBotCorpusTrainer(cbot)

#Now train the chatbot using this english corpus
trainer.train("chatterbot.corpus.english")

def responding(message):
    # Get a response to an input statement
    response=cbot.get_response(message)
    print("Bot:",response)


exit_List =['bye','exit','Exit','EXIT','Bye','BYE','Goodbye']
print("The bot is ready! Lets chat !!")
user_Inp =input("You:")
while(user_Inp not in exit_List):
    responding(user_Inp)
    user_Inp =input("You:")

print("Good bye hooman :D")
