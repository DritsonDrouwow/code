import pyttsx3
import speech_recognition as sr
import random

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("?????? Speak Now.....")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand. ")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""


def get_samples(command):
    get_samples = ["Why did the skeleton go to the blood bank? He wanted to work for a living.", 
                 "My eye doctor said my vision is getting worse. I guess I didn't see that coming.",
                 "Did you hear about the mathematician whos afraid of negative numbers? He will stop at nothing to avoid them.",
                 "What's a cat's favorite song? Three Blind Mice."]
    if "joke" in command:
        joke = random.choice(get_samples)
        speak(joke)
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        
    else:
        speak("Oops, I didn't catch that. Please try again.")
    


def main():
    speak("Voice assistant activated. Say something! ")
    while True:
        command = get_audio()
        if command and not get_samples(command):
            break
if __name__ == "__main__":
    main()
