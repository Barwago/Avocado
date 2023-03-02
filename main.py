import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Wait for a bit")
        query = r.recognize_google(audio, language='en-US')
        print(f'You just said: {query}\n')
        speak(f'You just said: {query}')
    except Exception as e:
        print(e)
        speak('Please repeate that')
        query='none'
    return query    

def wishing():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        print("Good morning")
        speak("Good morning")
    elif hour >= 12 and hour<17:
        print("Good afternoon")
        speak("Good afternoon")
    elif hour >= 17 and hour<21:
        print("Good evening")   
        speak("Good evening")     
    else:
        print("Good night")
        speak("Good night")

if __name__ == '__main__':
    wishing()
    query = commands().lower()