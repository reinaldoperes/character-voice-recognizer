from email.mime import audio
import speech_recognition as sr
import pyttsx3
import moviepy.editor as mp

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
  # Initialize the engine
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()
 
# using microphone as source  
with sr.Microphone() as source2:
  # wait for a second to let the rocognizer adjust the energy threshold based on
  # the surrounding noise level
  r.adjust_for_ambient_noise(source2, duration=0.2)
  
  # listen for the user's input
  audio2 = r.listen(source2)
  
  # using google to recognize the audio
  myText = r.recognize_google(audio2, language="pt-BR").lower()
  
  print("You said: ", myText)
  SpeakText(myText)
  