from time import ctime
import time
import os
import requests, json

#listen import
import speech_recognition as sr

#speak import
import pyttsx3
import time
from pygame import mixer
from gtts import gTTS

#LLM import
import openai

#Global Variables
openai.api_key = OPEN_AI_API_KEY

while True:
    # Use the listen function from voice_input.py
    data = listen()

    # If the user says 'exit', break the loop
    if data.lower() == 'exit':
        break

    # Send data to GPT-3 and get response
    response = chat(data)

    # Use the speak function from voice_output.py
    speak_espeak(response)

"""
This module captures audio from the microphone and converts it to text using Google's Speech Recognition API
- listen: .
"""
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("you said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

"""
This module will use the eSpeak library to convert the given text to speech and play the resulting audio.
"""
def speak_espeak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[17].id)
    engine.say(text)
    engine.runAndWait()

"""
This module will use OpenAI's API to generate a response to the given prompt.
"""
def chat(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=[{"role":"user","content":prompt}],
    )
    response_text = response['choices'][0]['message']['content']
    return response_text