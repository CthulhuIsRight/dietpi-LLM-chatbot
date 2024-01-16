from time import ctime
import os
import requests, json
import speech_recognition as sr  # listen import
import pyttsx3  # speak import
import openai  # LLM import

# Initialize OpenAI API Key
openai.api_key = os.getenv("OPEN_AI_API_KEY")

def listen():
    """
    Captures audio from the microphone and converts it to text using Google's Speech Recognition API.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = recognizer.listen(source)

    try:
        data = recognizer.recognize_google(audio)
        print("You said: " + data)
        return data
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print(f"Request Failed; {e}")
        return ""

def speak_espeak(text):
    """
    Uses the eSpeak library to convert the given text to speech and play the resulting audio.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Ensure the voice index exists to avoid errors
    voice_index = 17 if len(voices) > 17 else 0
    engine.setProperty('voice', voices[voice_index].id)
    engine.say(text)
    engine.runAndWait()

def chat(prompt):
    """
    Uses OpenAI's API to generate a response to the given prompt.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response['choices'][0]['message']['content']

def main():
    while True:
        data = listen()
        if data.lower() == 'exit':
            break
        response = chat(data)
        speak_espeak(response)

if __name__ == "__main__":
    main()