#Consider phasing out this module
"""
This module will use Google's Text-to-Speech API to convert the given text to speech and play the resulting audio.
"""
def speak_googleTTS(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.1)  # delay for a short period