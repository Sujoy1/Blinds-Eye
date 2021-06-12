import os
from gtts import gTTS

def text_to_speech(label):
    #Converting text to speech
    myobj = gTTS(text=label, lang='en', slow=False)
    #Saving the converted audio file into the same directory
    myobj.save("Outputs/output.mp3")
    #Play the converted file
    os.system("start Outputs/output.mp3")
