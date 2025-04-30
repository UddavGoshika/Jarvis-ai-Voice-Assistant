#this is about  the text to speech module :
import pyttsx3

engine=pyttsx3.init()
engine.setProperty("rate",150)

def speak(text):
  engine.say(text)
  engine.runAndWait()
speak("hello,there I am Ai VOice ASSITANT first module that is text to speech...")  

#this is about the speech to text module :  


import speech_recognition as sr

r = sr.Recognizer() #intializing the recognizer method to work 

while(1):


  try:
    with sr.Microphone() as source:

      audio = sr.listen(source)
      text = r.recoginze_google(audio)
      text = text.lower()
      print(text) 
   except sr.RequestError as e:
        print("Could not request results:".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")
from googlesearch import search
def google_search(query):
  try:
    results = list(search(query,num_results=3))
    return '\n'.join(results)
def realtime_chat_response(prompt):
  Google_search(prompt)
  return result 



def opening_instagram():
    speak("Opening Instagram")
    webbrowser.open("https://www.instagram.com")
    time.sleep(1)
    speak('instagram is opened sir')

def opening_facebook():
    speak("Opening Facebook")
    webbrowser.open("https://www.facebook.com")
    time.sleep(1)
    speak('facebook is opened sir')

def opening_whatsapp():
    speak("Opening WhatsApp")
    webbrowser.open("https://web.whatsapp.com")
  
  
  
