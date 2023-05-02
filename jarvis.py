import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes
from ecapture import ecapture as ec


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Gentleman") 
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Geltlemen...")

    else:
        speak("Good Evening Engineer Dipesh Paudel")

    speak ("I am Jarvis a robot at your service. How can I help you?")

def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")


def takeCommand():
    #It takes mic input and convert to text speech output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Pardon me Gentleman")
        speak("Pardon me Gentleman!")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('er.dipeshpaudel@gmail.com','your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
            query = takeCommand().lower()

            #Logic for executing the tasks
            if 'wikipedia' in query:
                speak ('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak ("According to Wikipedia...")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak ("Opening Youtube...")
                webbrowser.open("youtube.com")
                
            elif 'open google' in query:
                speak (" Opening Google")
                webbrowser.open("google.com")

            elif 'modern engineer' in query:
                speak ("Opening Your Youtube Channel")
                webbrowser.open("https://www.youtube.com/channel/UCzhz1JecArdYlHo2zu_2B3Q")

            elif 'GPT' in query:
                speak (" Opening ChatGPT")
                webbrowser.open("https://chat.openai.com/")

            elif 'open stackoverflow' in query:
                speak (" Opening Stackoverflow")
                webbrowser.open("stackoverflow.com")
                 
            elif 'play music' in query:
                speak ("Playing random music")
                music_dir = 'F:\\Music'
                songs = os.listdir(music_dir)
                randomSong = random.randint(0, 100)
                print (randomSong)
                print (f"Random selected: {songs[randomSong]}")
                os.startfile(os.path.join(music_dir, songs[randomSong]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Gentlemen, the time is {strTime}")

            elif 'open visual studio code' in query:
                speak ("Opening Visual Code Studio")
                codePath = "C:\\Users\\GenZ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'joke' in query:
                speak("Here! I got a joke for you........")
                jokes= pyjokes.get_joke()
                print(jokes)
                speak(jokes)
                speak ("ha ha ha ha......")
                speak("would you like to listen another joke?")



            elif 'send email' in query:
                try:
                    speak("What do you want to send?")
                    content = takeCommand()
                    to = "dipeshpaudel999@gmai.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak ("Sorry my friend, I coundn't send email")

            elif 'open college dashboard' in query:
                speak ("Opening College Dashboard")
                webbrowser.open("http://112.196.50.43/login.asp")

            elif 'open university portal' in query:
                speak ("Opening Punjab Technical University Portal")
                webbrowser.open("https://www.ptuexam.com/")

            elif 'open university support' in query:
                speak ("Opening Punjab Technical University support center")
                webbrowser.open("http://support.ptu.ac.in/Login.aspx")

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'hello jarvis' in query:
                speak("Hello gentleman! How may i help you")
 
            elif 'thank you' in query or "thanks" in query:
                speak("It was my pleasure gentleman!")
 
            elif "who are you" in query:
                speak("I am an AI bot to make human life convenient")

            elif "i love you" in query:
                speak ("That's so sweet of you! I love you too.")
                speak ("By the way you are looking handsome today!")

            elif "best football player" in query:
                speak ("Oh My God! This is best question somebody can ask me.")
                speak ("The best football player of all time is non other then The living legend Cristiano Ronaldo, AKA CR7........ Suieeeee")

 
