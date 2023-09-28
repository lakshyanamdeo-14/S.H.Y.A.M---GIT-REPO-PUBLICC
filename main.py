import os
import speech_recognition as sr
import pyaudio
import pyttsx3

import datetime
import webbrowser
import random
import wikipedia
import requests
from bs4 import BeautifulSoup
import pyautogui


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math




#initiating the Speak engine and deciding the voice as david (default voice)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



#say function it takes sentence to be spoken as an Input and speaks it

def say(audio):
    engine.say(audio)
    engine.runAndWait()



# take command function which takes the user command and tells us what we just said

def takecommand():
    global query
    r=sr.Recognizer()
    r.energy_threshold=500


    with sr.Microphone() as source:
        print("Listening .....")
        r.adjust_for_ambient_noise(source)
        audio_input=r.listen(source)

    try:
        print("Recognising...")
        query= r.recognize_google(audio_input,language="en-in")

        print(f"You said : {query}")
    except Exception as e:
        print("Iam sorry sir, Iam unable to recognise the what you said ?.")
        return "None"
    return query
def time():

    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    say(f"Sir, the time is {strTime}")


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        say("Good Morning sir ")
    elif hour > 12 and hour <= 15:
        say("Good afternoon Sir")
    elif hour > 15 and hour <= 24:
        say("Good Evening sir")
    else:
        say("Hello Sir Iam here as your assistant")

def open_file(address):
    pass

    os.startfile(address)
def stone():

    l=["stone",'paper','scissors']
    say("Let's Play Stone paper scissor !!!")
    say(" Instructions are like this , You will enter the choice among stone, paper and scissors ")
    say(" and then I will say mine , if I won I will get 1 point and If you won You will get one point")
    say(" Shall we start ? , Type yes or No")
    answer = input('>>>  ').lower()
    if answer=='yes':
        say(" Okaayy Let's Gooo")
        say("Type your answer")
        user = input(">>>   ")
        say('My Turn')
        a=random.choice(l)
        say(" MY Answer is :" )
        say(a)
        if a =='stone' and user =="stone":
            say("Match Tied")
        elif a =='stone' and user =='paper':
            say('You won ')

    





while True:

    inputt= takecommand().lower()
    


    if "hello" in inputt:
        say("Hello Sir , My self Shyaam and Iam your personal assistant ")
        say(" What can I do for you ?")
   

    elif 'open google' in inputt:
        webbrowser.open("google.com")
    elif 'sleep' in inputt:
        say("Sleeping Mode, ON")
        quit()
    elif 'youtube' in inputt:
        say("opening Youtube")
        webbrowser.open('https://www.youtube.com/')
    elif 'shopping' in  inputt :
        say('let mr check for you on Amazon')
        webbrowser.open('https://www.amazon.in/')
    elif 'time' in inputt :
        time()
    elif 'hello' in inputt:
        wish()

    elif 'facebook ' in inputt:
        say('opening Facebook')
        webbrowser.open('https://www.facebook.com/')






    elif "music" in inputt:
        say(" PLaying your favorite music")
        webbrowser.open('https://youtu.be/AETFvQonfV8')
    
  
    

        



    elif "harvard" in inputt:
        say("Opening harvard university official website")
        webbrowser.open("https://www.harvard.edu/programs/")
    elif "instagram" in inputt:
        say('opening instagram')
        webbrowser.open("instagram.com")

    elif 'college' in inputt:
        webbrowser.open('https://www.stthomascollegebhilai.in/')



    elif 'stress' in inputt:
        say('wait Sir , I Have solution for it .!!')
        webbrowser.open('https://youtu.be/6W5QsfjdERE')




    elif 'sleep' in inputt:
        say('Have a Good Day Sir !')
        quit()

    elif 'weather' in inputt:
        say('can you mention the city please sir ? ')
        city= takecommand().lower()
        search = f'temperature in {city}'
        url = f"https://www.google.com/search?q={search}"

        r= requests.get(url)
        data = BeautifulSoup(r.text,'html.parser')
        temp = data.find('div',class_='BNeawe').text
        say(f'Temperature in {city} is around {temp}')
        say('I have also opened the weather chart on the screen sir , just have a look over it ')
        print(f'temp = {temp}')
        webbrowser.open(f'https://www.google.com/search?q=weather+{city}&sxsrf=AJOqlzXoS5ZM1ArqC2k_3fsUmCOxvOp2Hg%3A1674556030599&ei=frLPY6OcJPvgseMPuouCyA8&ved=0ahUKEwij0_Cq_9_8AhV7cGwGHbqFAPkQ4dUDCA8&uact=5&oq=weather+{city}g&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQgAQQRhCAAjIKCAAQgAQQFBCHAjIFCAAQgAQyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwEyCAgAEIAEEMsBMgUIABCABDIKCAAQgAQQAhDLATIFCAAQgAQ6CggAEEcQ1gQQsAM6BwgAELADEEM6BQgAEJECOhAIABCABBAUEIcCELEDEIMBOggIABCxAxCDAUoECEEYAEoECEYYAFCNBVjCDmDyEmgBcAF4AYABpwWIAekMkgEHMi00LjUtMZgBAKABAcgBCsABAQ&sclient=gws-wiz-serp')
        print(inputt)
    


    elif 'wikipedia' in inputt:
        say('please say type query')
        search = input('Enter the Query: ')
        query = wikipedia.summary(search , sentences =2) 
        say(f"Accoridng to wikipedia {query}")

        
    elif'whatsapp' in inputt:
        say('Opening Whatsapp')

        webbrowser.open('https://web.whatsapp.com/')
    
    elif 'mail' in inputt:
        say('opening EMail')
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    
    else:
        say("Couldn't able to understand sir , please repeat")
        print(" Couldn't able to understand sir , please repeat")

