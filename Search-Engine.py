import pyttsx3
import speech_recognition as sr
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
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
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    print("how may i help you sir")
    speak("how may i help you sir")
    while True:
        query = takeCommand().lower()
        print("Searching: " + query) 

        if "wolfram alpha" in query:
            speak("what do you search want to search on wolfram alpha")
            qs = takeCommand().lower()
            webbrowser.get(chrome_path).open("https://www.wolframalpha.com/input/?i="+qs)
        elif "google" in query:
            speak("what do you search want to search on google")
            qa = takeCommand().lower()
            webbrowser.get(chrome_path).open("https://www.google.com/?q="+qa)
        elif "wikipedia" in query:
            speak("what do you search want to search on wikipedia")
            qd = takeCommand().lower()
            webbrowser.get(chrome_path).open("https://en.wikipedia.org/wiki/"+qd)
        elif "youtube" in query:
            speak("what do you search want to search on youtube")
            qe = takeCommand().lower()
            webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query="+qe)
        elif "github" in query:
            speak("what do you search want to search on github")
            qi = takeCommand().lower()
            webbrowser.get(chrome_path).open("https://github.com/search?q="+qe)
