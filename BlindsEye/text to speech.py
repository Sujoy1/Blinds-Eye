from gtts import gTTS 
  
# import Os module to start the audio file
import os 


myText = " My name is Krishna"

# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")


# Play the converted file 
os.system("start output.mp3")