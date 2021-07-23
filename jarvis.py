import os
import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice = engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Good Morning boss!")
        speak("good morning boss!")

    elif 12 <= hour < 17:
        print("Good Afternoon boss!")
        speak("good afternoon boss!")

    else:
        print("Good Evening boss!")
        speak("good evening boss!")

    speak("I am Jarvis, how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        speak("Listening..........")
        r.energy_threshold = 350
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        speak("Sorry, i did not hear properly, Say that again please....")
        return "None"

    return query


if __name__ == '__main__':
    wishme()
    trn = datetime.datetime.now().strftime("%H : %M")
    while True:
        query = takeCommand().lower()
        # command to search wikipedia
        if 'wikipedia' in query or 'who is' in query:
            print("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            speak("Searching wikipedia")
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'open linkedin' in query:
            speak("opening linkedin")
            webbrowser.open("linkedin.com")

        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")

        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp' in query:
            speak("opening whatsapp for you")
            webbrowser.open("web.whatsapp.com")

        elif 'the time' in query:
            print(f"The time right now is {trn}")
            speak(f"The time right now is {trn}")

        elif "what's up" in query or "what is going on" in query or "what's going on" in query:
            print(f"Nothing much. its {trn} right now.")
            print("I can open YouTube or can play some music for you. Just say play music")
            speak(f"Nothing much. its {trn} right now.")
            speak("i can open youtube or can play some music for you. Just say play music")

        elif 'who are you' in query or 'your name' in query:
            print("My name is Jarvis. I am a virtual desktop assistant made by Mr. Harsh Gupta. How may i help you?")
            speak("My name is Jarvis. I am a virtual desktop assistant made by Mr. Harsh Goupta. How may i help you?")

        elif "who made you" in query or "who created you" in query:
            print("I have been created by Mr. Harsh Gupta.")
            speak("I have been created by Mr. hersh gupta.")

        elif 'open code' in query:
            speak("opening visual studio code")
            path = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open teams' in query:
            speak("opening microsoft teams")
            path = '''C:\\Users\\harsh\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"'''
            os.startfile(path)

        elif 'open pycharm' in query:
            speak("opening pycharm ")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'open vlc' in query:
            path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            speak("opening vlc media player")
            os.startfile(path)

        elif 'play music' in query or 'play song' in query or 'play some music' in query or 'play a song' in query:
            speak("Sure sir, enjoy the song")
            print("i will stop listening for 20 seconds from now")
            speak("i will stop listening for 20 seconds from now ")
            music_path = "D:\\songs"
            songs = os.listdir(music_path)
            a = random.randint(0, len(songs))
            os.startfile(os.path.join(music_path, songs[a]))
            time.sleep(20)

        elif "who i am" in query or 'who am i' in query:
            speak("If you talk then definitely your human.")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            print("It's good to know that your fine")
            speak("It's good to know that your fine")

        elif 'reason for you' in query:
            print("I was created as a Minor project by Mr. Harsh gupta ")
            speak("I was created as a Minor project by Mister Harsh gupta ")

        elif 'joke' in query or 'jokes' in query:
            jok = pyjokes.get_joke()
            print(jok)
            speak(jok)

        elif 'quit' in query:
            print("Sure Sir, Thanks for letting me help you. Have a good day.")
            speak("sure sir, thanks for letting me help you. Have a good day.")
            exit()

        elif 'exit' in query:
            print("Sure Sir, Thanks for letting me help you. Have a good day.")
            speak("sure sir, thanks for letting me help you. Have a good day.")
            exit()
