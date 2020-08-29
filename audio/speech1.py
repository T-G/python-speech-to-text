import speech_recognition as sr

filename="pdaLR.wav"
# create Recognizer object
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_source = r.listen(source)
    try:
        text=r.recognize_google(audio_source)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
        print("Sorry.. Try again")
    