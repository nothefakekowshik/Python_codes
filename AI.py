import pyttsx3
import speech_recognition as sr
import datetime 

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate


stri="I love dani daniels"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(name):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning "+str(name)+" have a great day!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon"+str(name) +"How is your day going?")
    else:
        speak("Good evening"+str(name)+" hope you had a great day")
    #speak("time is "+hour)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("RECOGNIZING..")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        if(query=="stri"):
            speak("That's cool Dani loves you too")
    except:
        # print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    speak("Hello this is your personal assistant,Could you please type your name?")
    print("Name please:")
    name=input()
    #wishme(name)
    x = datetime.datetime.now()
    time=x.strftime("%X")
    mtime=time[:2]
    mtime=int(mtime)
    if mtime>= 0 and mtime < 12:
        speak("Good morning "+str(name)+" have a great day!")
    elif mtime>= 12 and mtime < 18:
        speak("Good afternoon"+str(name) +"How is your day going?")
    else:
        speak("Good evening"+str(name)+" hope you had a great day")
    speak("Enter the speech you would like to talk to me!")
    speech=input()
    if(speech.lower()==stri.lower()):
        speak("woah! Thats cool,Dani loves you too!")
    else:
        speak("That's ok! I'm here to help you Bye")
    
    #speak("talk now")
    
    #takecommand()