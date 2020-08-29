import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio = r.listen(source)

    # recognize speech using Google
try:
    print("Google thinks you said '" + r.recognize_google(audio) + "'")

except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Google error; {0}".format(e))