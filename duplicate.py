import pyttsx3
import datetime
# import pyAudio
import wikipedia
import webbrowser
import os
import  random
import smtplib
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
    except Exception as e:
        speak("error here")
    server.ehlo()
    server.starttls()
    server.login( "your email" ,"your address" )
    server.sendmail("your email" , to, content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir! jarvis this side")
    elif hour>=12 and hour <18:
        speak("good Afternoon Sir! jarvis this side")
    else:
        speak("Good Evening Sir! jarvis this side")

    speak("Hope you are doing great......How may I help you?")

def takeCommand():
    #It takes microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold =1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return  "None"
    return query




if __name__ == "__main__":

    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            speak("Launching youtube...")
            url = "https://www.youtube.com/"
            webbrowser.register('chrome',

                                None,

                                webbrowser.BackgroundBrowser(

                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

            webbrowser.get('chrome').open(url)
        elif 'open google' in query:
            # webbrowser.open("google.com")
            speak("Launching google...")
            url = "https://www.google.com/"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'open official mail' in query:
            # webbrowser.open("google.com")
            speak("Opening official mail...")
            url = "official mail link (sign in karke rakho)"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'open personal mail' in query:
            # webbrowser.open("google.com")
            speak("opening personal mail...")
            url = "apni personal mail ki link"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'time table' in query:
            # webbrowser.open("google.com")
            speak("Opening Time Table...")
            url = "jaha par time table ki file hai uska address"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'open whatsapp' in query:
            # webbrowser.open("google.com")
            speak("Launching Whatsapp...")
            url = "https://web.whatsapp.com/"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'join physics class' in query:
            # webbrowser.open("google.com")
            speak("Joining Physics class...")
            url = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_MWNjYWRkZWYtOTEzOC00ZWEzLTk2YTQtODBhNTdjMGZlNjRj%40thread.v2/0?context=%7b%22Tid%22%3a%22a6de9407-2d24-407d-81e6-941b053c301a%22%2c%22Oid%22%3a%2269e930c2-e480-4088-acfe-5ecad62c1900%22%7d"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'join computer class' in query:
            # webbrowser.open("google.com")
            speak("Joining CP class...")
            url = "https://teams.microsoft.com/l/meetup-join/19:meeting_NjFkNWJkNDMtOGU0Yy00NWNhLThmMmUtZWU0ZmNiOWUzMTlh@thread.v2/0?context=%7B%22Tid%22:%22a6de9407-2d24-407d-81e6-941b053c301a%22,%22Oid%22:%226b4ca91f-0a12-40d0-b386-f3667f31bf11%22%7D"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'join mpp class' in query:
            # webbrowser.open("google.com")
            speak("Joining MPP class...")
            url = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_MDA0ZTNkYjEtNWM0Mi00NjYyLWJiNTUtNTBlNjk2NjkzOTQ3%40thread.v2/0?context=%7b%22Tid%22%3a%22a6de9407-2d24-407d-81e6-941b053c301a%22%2c%22Oid%22%3a%22ac3ac72c-9af3-47ae-a4c3-f64214b9f05d%22%2c%22MessageId%22%3a%220%22%7d"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'join maths class' in query:
            # webbrowser.open("google.com")
            speak("Joining Maths class...")
            url = "https://teams.microsoft.com/l/meetup-join/19%3A013ba964d4914d2387fb5b86c292e70e%40thread.tacv2/1616551074518?context=%7B%22Tid%22%3A%22a6de9407-2d24-407d-81e6-941b053c301a%22%2C%22Oid%22%3A%22106db79c-6eb3-4232-8af0-6d6d0e7e6c85%22%7D"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'join electrical class' in query:
            # webbrowser.open("google.com")
            speak("Joining BEC class...")
            url = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZWVmOTMwNzEtMmNmNC00ZDIzLWI3NDItMTllNWM0NWZjNTYy%40thread.v2/0?context=%7b%22Tid%22%3a%22a6de9407-2d24-407d-81e6-941b053c301a%22%2c%22Oid%22%3a%227ed62679-4381-42d3-a869-1da0615371b6%22%7d"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'join graphic class' in query:
            # webbrowser.open("google.com")
            speak("Joining EG class...")
            url = "https://teams.microsoft.com/l/meetup-join/19:69012fa7fc97423ab6924667ead090bd@thread.tacv2/1616388632095?context=%7B%22Tid%22:%22a6de9407-2d24-407d-81e6-941b053c301a%22,%22Oid%22:%228f0d4c70-768f-4901-ba2e-99d3a8362be2%22%7D"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'join graphic practical' in query:
            # webbrowser.open("google.com")
            speak("Joining EG pratical class...")
            url = "meet.google.com/dtn-pvrz-dgj(apne subgroup ka link daaloa)"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'open classroom' in query:
            # webbrowser.open("google.com")
            speak("Launching classroom...")
            url = "https://classroom.google.com/u/0/h"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        elif 'open codechef' in query:
            # webbrowser.open("google.com")
            speak("Launching codechef...")
            url = "https://www.codechef.com/"
            webbrowser.register('chrome',
                                None,
                                webbrowser.BackgroundBrowser(
                                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)


        elif 'play music' in query:
            music_dir = "C:\\Users\\HP\\Music (jaha par music store kiye hue hai)"
            songs=os.listdir(music_dir)
            # print(songs)
            a=random.randint(0,204)
            print(f"Now Playing {songs[a]}")
            os.startfile(os.path.join(music_dir,songs[a]))

        elif 'tell time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening vs code...")
            codePath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe (vs code ka target address daalo)"
            os.startfile(codePath)

        # elif 'open teams' in query:
        #     codePath="C:\\Users\\HP\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart\\Teams.exe"
        #     os.startfile(codePath)

        elif 'write mail' in query:
            try:
                speak("To whom should I mail Sir?")
                name="None"
                while name == "None":
                    name=takeCommand().lower()
                    if name=="None":
                        speak("Say that again please")

                contact={"abc": "abc"}
                speak("What should I say")
                content=takeCommand()
                # print(content)
                to=contact[name]
                sendEmail(to,content)
                speak("Email has been sent!")
            except:
                print("Sorry..Email not send")
                speak("Email not send")




        elif 'thank you' in query:
            speak("anytime for you sir!!")

        elif 'turn off' in query:
            speak("Ok Sir")
            exit()