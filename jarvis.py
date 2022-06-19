import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import smtplib
import random
import time
import requests
import json
from bs4 import BeautifulSoup
from PyLyrics import *
import pyautogui
from PIL import ImageGrab

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# my friends numbers
dicf = {
    'yashu': '6300083122',
    'akhil': '6281213336',
    'dad': '9642211977',
    'jaya': '99085824888',
    'jyotsna': '8522850465',
    'karthikeyan': '9032461711',
    'nikitha': '7981993505',
    'nikita best friend': '7569259500',
    'mahidhar': '6301227343',
    'pragati': '8106300514',
    'sri vidya': '7093389499',
    'sushma': '9441620112',
    'today': '7075255954',
    'vamshi': '9182062791',
    'you should': '9493648806',
    'mohan': '7989594735',
    'rohit': '9440250540'
}


def speak(text):
    """This function is used for speech . That means it takes the input as a text and a turns it into a speech"""
    engine.say(text)
    engine.runAndWait()


def search(dicf):
    speak("yeah tell me the name whom you want the number")
    names = takecommand().lower()
    try:
        print(dicf[names])
        speak(dicf[names])
        speak("do you want to search any other numbers")
        choice = takecommand().lower()
    except Exception as e:
        speak("Sorry sir there is no such numbers")
        speak("Do you want to search any other numbers")
        choice = takecommand().lower()
        if "yes" in choice:
            search(dicf)
        if "no" in choice:
            return 0

def screenshot():
        image = ImageGrab.grab().convert('L')
        return image

def checkmsg():
    time.sleep(12)
    image = screenshot()
    data = image.load()
    d = 0
    message = 0
    a = 330
    b = 345      
    while(d<=5):
        number = 0
        for i in range(620,640):
            for j in range(a,b):
                if data[i,j] <200:
                    number+=1
        if number!=0:
            message+=1
        d+=1
        a+=108
        b+=108
    
    return message


def alarm():
    hour = datetime.datetime.hour()
    minute = datetime.datetime.minute()
    if hour == 15 and minute == 46:
        return True
    else:
        return False

def wakeup():
    wake = takecommand().lower()
    if "wake up" in wake or "makeup" in wake:
        return
    else:
        while(True):
            wake = takecommand().lower()
            if "wake up" in wake:
                return

    pass


def wishme():
    """This function is used to wish the user by using speak function"""
    hour = int(datetime.datetime.now().hour)
    mins = int(datetime.datetime.now().minute)
    sec = int(datetime.datetime.now().second)

    if hour >= 0 and hour <= 12:
        speak("good morning sir")
    elif hour > 12 and hour <= 15:
        speak("good afternoon sir")
    elif hour > 15 and hour <= 19:
        speak("good evening sir")
    elif hour > 19 and hour <= 24:
        speak("good night sir")

    speak(f"Now the time is {hour} {mins}")
    speak("I am jarvis , how may i help you sir")


def takecommand():
    """This function is used to to take command from the user via voice """
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.energy_threshold = 4000
        r.pause_threshold = 1
        print("listening....")
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said : {query}")
        return query

    except Exception as e:
        query = takecommand()
        return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("yashuatla6@gmail.com", "yashwanth")
    server.sendmail("yashuatla@gmail.com", to, content)
    server.close()


def playmusic():
    songs = os.listdir(r"C:\sid sriram songs")
    song = random.choice(songs)
    speak("playing music in your directory sir")
    os.startfile(os.path.join(r"C:\sid sriram songs", song))

def main():
    wishme()
    while True:
        # if alarm() == True:
        #     speak("wake up sir it is 3:46 now it is high time to wake up"*10)
        #     speak("sir tell me good morning to assure that you had woke up")
        #     good = takecommand().lower()
        #     if "good morning" not in good:
        #         speak("sir tell me clearly ,by hearing your voice i am thinking that you are still in sleep mode only")
        #         speak("Would you want me to make a phone call to you dad")
        #         user = takecommand()
        #         if "no" in user:
        #             speak("Then tell me clearly good morning sir")
        #             if "good morning" in user:
        #                 speak("good morning sir,go and wash your face sir,i will play some music for you")
        #                 songs = os.listdir(r"C:\sid sriram songs")
        #                 song = random.choice(songs)
        #                 speak("playing music in your directory")
        #                 os.startfile(os.path.join(r"C:\sid sriram songs", song))

        query = takecommand().lower()

        if "wikipedia" in query:
            # This is for searching something in wikipedia
            speak("searching in wikipedia")
            query = query.replace("wikipedia", "")
            print(query)
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak("According to wikipedia")
            speak(results)
            break
        elif "open google" in query:
            # This is for searching something in google
            speak("tell me what you wanna search in google sir")
            sear = takecommand()
            speak(f"searching {sear} in google")
            webbrowser.open(f"https:\\google.com\search?q={sear}")
        elif "open youtube" in query:
            # This is for playing something in youtube
            speak("tell me what you wanna play in youtube sir")
            searches = takecommand()
            speak(f"playing {searches} in youtube")
            pywhatkit.playonyt(searches)
            
        elif "open spotify" in query:
            # This is for opening spotify in our pc
            location = r"C:\Users\yash\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\spotify"
            try:
                os.startfile(location)
            except Exception as e:
                speak("sorry sir i can't find spotify")
                speak(
                    "Enter the exact location of spotify in this pc so that i can save that loaction to open whenever you want"
                )
                location = input()

        elif "open vs code" in query:
            # This is to open vs code in our laptop if it is there
            try:
                locationv = r"C:\Users\yash\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code"
                os.startfile(locationv)
            except Exception as e:
                speak("sorry sir i can't find spotify")
                speak(
                    "Enter the exact location of visual studio code in this pc so that i can save that loaction to open whenever you want"
                )
                location = input()
            break
        elif "time now" in query:
            # This is to know time
            hour = int(datetime.datetime.now().hour)
            mins = int(datetime.datetime.now().minute)
            speak(f"The time now is {hour}:{mins}")

        elif "send email" in query:
            # This is to send email to any person . But here you have to enter the email . It is somewhat complicated to tell the email address no
            try:
                speak("Whom you want to send your mail")
                mail = input("Tell me the mail of that person : ")
                speak("tell me what you wanna send")
                speak("Tell me how much time will it take to say the content")
                choice = input()
                content = takecommand(choice)
                sendEmail(mail, content)
                speak("Email has been sent")
            except:
                speak("sorry i am unable to send the mail sir")
            break
        elif "play music" in query or "play some music" in query:
            # This statement is written to play the offline music in your directory
            playmusic()

        elif "motivation" in query:
            # This statement is to give the motivation while you are disappointes or something
            pywhatkit.playonyt("motivation for study")
            break
        elif "goodbye" in query:
            # you can stop the programme if you want by saying good bye
            speak("good bye sir, have a nice day")
            break
        elif "hello jarvis" in query:
            speak("Hello sir good to see you")
        elif "how are you" in query:
            speak("I am fine sir,What about you")
            choice1 = takecommand()
            if "bad" in choice1 or "not good" in choice1 or "not fine" in choice1:
                speak("why sir what happened")
                speak(
                    "It is better to take rest sir , i will remind you in 15 minutes"
                )
                i = 0
                while (i <= (15 * 60)):
                    i += 1
                    time.sleep(1)
                speak("The time is over sir wake up please")
                speak(
                    "I am playing some music to cheer you up sir,relax some time"
                )
                playmusic()

            if "good" in choice1 or "fine" in choice1 or "not bad" in choice1:
                speak("It was nice to hear it from you sir")

        elif "open whatsapp" in query:
            # This statement is there to open your what's app
            speak("yes sir i am opening your what's app")
            webbrowser.open(r"https://web.whatsapp.com/")

        elif "i love you" in query:
            speak("sorry sir i am in love with your wifi")

        elif "boring" in query:
            # This statement is written to play some funny videos
            lis = [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                19, 20, 21, 22, 23, 24, 25
            ]
            comp = random.choice(lis)
            speak("I will play some funny videos for you")
            list1 = [1, 2, 3, 4, 5]
            choice5 = random.choice(list1)
            if choice5 == 1:
                pywhatkit.playonyt(f"shot on iphone meme compilation {comp}")
            if choice5 == 2:
                pywhatkit.playonyt("boss moment compilation")
            if choice5 == 3:
                pywhatkit.playonyt("funmoji videos")
            if choice5 == 4:
                pywhatkit.playonyt("funny videos")
            if choice5 == 5:
                pywhatkit.playonyt("respect tik tok compilation")
            break
        elif "current temperature" in query:
            # This statement is there to tell the current temperature
            search = "temperature in srikakulam"
            r1 = requests.get(f"https://google.com/search?q={search}").text
            data = BeautifulSoup(r1, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            print(temp)
            speak(f"The current temperature here is {temp}")

        elif "lyrics" in query:
            # This statement is there to provide the lyrics of the song you want
            speak("Tell me the song sir for which you want the lyrics")
            song = takecommand()
            speak("Who is the singr of that song sir")
            singer = takecommand()
            lyrics = (PyLyrics.getLyrics(singer, song))
            print(lyrics)
            break
        elif "send whatsapp message" in query:
            # This statement is there to send whatapp message to someone
            speak("sir do you want to send message now or a bit later")
            choice6 = takecommand()
            if "now" in choice6:
                speak(
                    "Tell me name of the person whom you want to send the message sir"
                )
                name1 = takecommand().lower()
                speak("Tell me the message you want to send sir")
                msg1 = takecommand()
                pywhatkit.sendwhatmsg_instantly(f"+91{dicf[name1]}", msg1)
            elif "later" in choice6:

                speak(
                    "Tell me name of the person whom you want to send the message sir"
                )
                name1 = takecommand().lower()
                speak(
                    "Tell me at what hour and minute you want to send the message"
                )
                time2 = takecommand()
                listtime1 = time2.split(" ")
                speak("Tell me the message you want to send sir")
                msg = takecommand()
                pywhatkit.sendwhatmsg(f"+91{dicf[name1]}", msg,
                                      int(listtime1[0]), int(listtime1[2]))
        elif "write in a funny" in query or "write something in a funny" in query:
            # This statement is there to write whatever you say in a png doctument
            speak("Tell me what do you wanna write sir")
            write = takecommand()
            speak("What name would you want to put to the file sir")
            name2 = takecommand()
            pywhatkit.text_to_handwriting(write, f"{name2}.png")
            speak(
                f"the words you had told is saved in the form of text in the name of {name2}.png"
            )

        elif "forgot the number" in query or "forget the number" in query:
            # This statement is there to tell the numbers of your friends
            search(dicf)
        elif "remember this" in query:
            speak("Tell me what you want to remember sir")
            remember = takecommand()
            if "remember" in remember:
                remember = remember.replace("remember", "")
            speak("tell me sir what is it")
            mainre = takecommand()
            with open("remember.txt", "a") as f:
                f.write(f"{remember} : {mainre}\n")

        elif "remind me" in query:
            # This statement is used to set the reminder for how much time you want
            for words in query:
                if words.isnumeric() == True:
                    timere = words
                if "minutes" in query:
                    time.sleep(timere * 60)
                elif "seconds" in query:
                    time.sleep(timere)
                elif "hours" in query:
                    time.sleep(timere * 60 * 60)
                speak("the time you had told to remind is over sir" * 3)
                playmusic()
        elif "last thing" in query and "to remember" in query:
            # This statemnt is user to know the last thing you told jarvis to remember
            try:
                with open("remember.txt", "r") as f:
                    content = f.read()
                    cont = content.split("\n")
                    numb = len(cont)
                    speak("The last thing you had told me to remember is that")
                    for words in cont:
                        if "my" in words:
                            words.replace("my", "your")
                    speak(cont[numb - 2])
            except:
                speak("sorry sir you didnt told anything to remember")
        elif "things" in query and "to remember" in query:
            # This statement is used to know all the things that you had told jarvis to remember
            try:
                with open("remember.txt", "r") as f:
                    content = f.read()
                    cont = content.split("\n")
                    i = 1
                    for words in cont:
                        speak(f"{i}   {words}")
                        if i - 1 == len(cont) - 2:
                            break
                        i += 1
            except:
                speak("sorry sir you did'nt told anything to remember")
        elif "that's it" in query:
            # This statement is used to put jarvis into sleep
            speak("ok sir enjoy the day")
            break
        elif "write something" in query:
            # This statement is to write something in microsoft word or notepad
            speak("tell me sir what do you want to write")
            matter = takecommand()
            speak("ok sir it is noted,where do you want me to write it")
            where = takecommand().lower()
            if "word" in where:
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word")
            if "note pad" in where or "notepad" in where:
                os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad")
                pyautogui.click(x=459, y=284)
            time.sleep(3)
            for words in matter:
                pyautogui.keyDown(words)
        elif "check whatsapp messages" in query:
            webbrowser.open("https://web.whatsapp.com/")
            message = checkmsg()
            if message == 0:
                speak("You did'nt got any messages")
            else:
                speak(f"you got messages from {message} members")
        elif "not today's plans" in query or "note today's plans" in query or "note tomorrow's plans" in query or "not today's plans" in query:
            speak("Tell me sir what is your plans today")
            plan = takecommand()
            plans = plan.split("next")
            with open("plan.txt","a") as f:
                for plan in plans:
                    f.write(f"{plan}\n")
            speak("ok sir it is noted")
        elif "tell me today's plans" in query or "tell me today's plan" in query:
            try:
                with open("plan.txt","r+") as f:
                    content = f.read()
                speak("today's plans are")
                i = 1
                planr = content.split("\n")
                while(i<=(len(planr) - 1)):
                    speak(f"{i} -- {planr[i - 1]}")
                    i+=1
            except:
                speak("sorry sir you did'nt tell any plans today")
        elif "animation" in query:
            pywhatkit.search("powtoon.com")
            time.sleep(3)
            pyautogui.click(300,450)
        elif "forward the video" in query or "forward video" in query:
            pyautogui.press("right")
            pyautogui.press("right")
        


if __name__ == "__main__":

    # wakeup()
    main()

# This is my jarvis project
    