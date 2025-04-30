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
def search_in_youtube():
    # Open YouTube in Chrome
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube, sir. Please wait.")
    time.sleep(5)  # Allow time for the browser to load YouTube (adjust based on speed)
    pyautogui.press('/')  # Navigate to the search bar

    # Ask what to search
    speak("What do you want to search on YouTube?")
    search_query = listen() # Replace with actual voice input function
    time.sleep(1)
    if search_query:
        speak(f"Searching for {search_query} on YouTube.")
        # pyautogui.hotkey('alt','tab')
        # # Navigate to the search bar (adjust depending on the browser tab focus)
        
        # Type each letter with animation
        for letter in search_query:
            pyautogui.typewrite(letter)
            time.sleep(0.05)  # Delay between each keystroke for animation effect
        
        pyautogui.press('enter')  # Trigger the search
        time.sleep(3)  # Wait for search results to load
        speak("Here are the search results for your query.")
    else:
        speak("I didn't catch that. Please try again.")  
  
  
  
