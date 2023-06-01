"""
This is AI based personal assistance (Jarvis) which will automate
the day to day task. 
"""
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")  # initialize the voice
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)


def speak(message):
    engine.say(message)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour) # gets the current time from the device
    if (hour >= 0) and (hour < 12):
        speak("Good Morning")
    
    elif (hour >= 12) and (hour < 18):
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello This is jarvis, how may i help you today")

def takecommand():
    """
    It takes the audio input from the mic of the device and returns the string
    output 
    """
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # wait for input upto 1 seconds
        message = r.listen(source)
    
    try:
        print("Reading Commands..")
        query = r.recognize_google(message, language="en-us")
        print(f"Command: {query}\n")

    except Exception:
        speak("I didn't get that sir")
        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    takecommand()