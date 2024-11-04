import google.generativeai as genai
from apikey import api_data 
import speech_recognition as sr # Converts my voice commands to text 
import pyttsx3 # Read out text output to voice. 
import webbrowser
import streamlit as st

Model = "gpt-3.5-turbo"
genai.configure(api_key = api_data)
model = genai.GenerativeModel('gemini-pro')

st.header("AI Assistance")

def Reply(question):
    txt = "provide answer in 2 sentences : " + question
    txt = model.generate_content(txt)
    result = txt.text
    return result.replace("**","")

# Text to speech 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("Hello How are you?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print('Listening .......')
        st.write("Listening .......")
        r.pause_threshold = 2 # Wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)
    try: 
        print('Recogninzing ....')
        st.write("Recogninzing ....")
        query = r.recognize_google(audio, language = 'en-in')
        print("User Said: {} \n".format(query))
        st.write("User Said: {} \n".format(query))
    except Exception as e:
        print("Say that again .....")
        return "None"
    return query

if __name__ == '__main__':
    while True: 
        query = takeCommand().lower()
        if query == 'none':
            continue
        
        # Specific Browser Related Tasks 
        if "open youtube" in query.lower(): 
            webbrowser.open('www.youtube.com')
        elif "open google" in query.lower(): 
            webbrowser.open('www.google.com')
        elif "exit" in query.lower():
            break 
        else:
            ans = Reply(query)
            print(ans)
            st.write(ans)
            speak(ans)