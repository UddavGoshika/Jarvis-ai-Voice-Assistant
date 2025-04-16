import pyttsx3

engine=pyttsx3.init()
engine.setProperty("rate",150)

def speak(text):
  engine.say(text)
  engine.runAndWait()
speak("hello,there I am Ai VOice ASSITANT first module that is text to speech...")  
  
