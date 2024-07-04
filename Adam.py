import pyttsx3
import speech_recognition as sr
import datetime
import applications as ap

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)  # Set the speaking rate (words per minute)

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning! How can I assist you?")
    elif 12 <= hour < 18:
        speak("Good Afternoon! How can I assist you?")
    else:
        speak("Good Evening! How can I assist you?")

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    response = f"The current time is {current_time}"
    speak(response)
    print(response)

def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    response = f"Today's date is {today}"
    speak(response)
    print(response)

def tell_day():
    day = datetime.datetime.now().strftime("%A")
    response = f"Today is {day}"
    speak(response)
    print(response)

def handle_search(command):
    query = command.replace("search", "", 1).strip()
    if query:
        ap.search_web(query)
    else:
        speak("What would you like me to search for?")

# Main program loop for speech recognition
def main():
    greet_user()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening....")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing......")

            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            if "hello" in command or "hey" in command:
                speak('Hi, how can I help you?')
            elif "adam" in command:
                speak('Yes, Adam here! How can I assist you today?')
            elif "time" in command:
                tell_time()
            elif "day" in command:
                tell_day()
            elif "date" in command:
                tell_date()    
            elif "open google" in command:
                ap.open_google()
            elif "open discord" in command:
                ap.open_discord()
            elif "open instagram" in command:
                ap.open_instagram()
            elif "open youtube" in command:
                ap.open_youtube()
            elif "open facebook" in command:
                ap.open_facebook()
            elif "open mail" in command:
                ap.open_mail()
            elif "open whatsapp" in command:
                ap.open_whatsapp()
            elif "open calculator" in command:
                ap.open_calculator()
            elif "open notepad" in command:
                ap.open_notepad()
            elif "search" in command:
                handle_search(command)
            elif "exit" in command or "quit" in command:
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("Hmm, I didn't catch that. Could you please repeat?")

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            speak("Sorry, I'm having trouble processing your request.")

# Run the main program
if __name__ == "__main__":
    main()
