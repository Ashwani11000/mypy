# for speech conversion 
from gtts import gTTS 
# To play the converted audio 
import os 



def t2s(speech_Text):
    speech = gTTS(text=speech_Text, lang='en', slow=False) 
    # saving as speech.mp3
    speech.save("speech.mp3") 
    # Play
    os.system("mpg321 speech.mp3") 

#for exit purpose    
exit_List= ["bye","exit","Goodbye","BYE","Bye","Exit","EXIT"]

speech_Text = "something"
while(speech_Text not in exit_List):
    speech_Text = input("User: ")
    t2s(speech_Text)


