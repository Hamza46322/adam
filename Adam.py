# main.py

import pyttsx3
import speech_recognition as sr
import random
import datetime
from openpyxl import load_workbook
import applications as ap

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Load Excel data
def load_excel_data(file_path):
    try:
        wb = load_workbook(file_path)
        user_sheet = wb['User']
        replies_sheet = wb['Replies']
        
        hello_list = [cell.value.lower() for cell in user_sheet['A'] if cell.value]
        how_are_you_list = [cell.value.lower() for cell in user_sheet['B'] if cell.value]
        
        reply_hello_list = [cell.value for cell in replies_sheet['A'] if cell.value]
        reply_how_are_you_list = [cell.value for cell in replies_sheet['B'] if cell.value]
        
        return hello_list, how_are_you_list, reply_hello_list, reply_how_are_you_list
    except Exception as e:
        print(f"Error loading Excel data: {e}")
        return [], [], [], []

# Example usage with specific file path
file_path = r"C:\Users\hamza\adam\file.xlsx"  # Raw string for Windows path
hello_list, how_are_you_list, reply_hello_list, reply_how_are_you_list = load_excel_data(file_path)

# Main program loop for speech recognition
def main():
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                print("Recognizing...")

            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            if any(phrase in command for phrase in hello_list):
                greet_user()
            elif any(phrase in command for phrase in how_are_you_list):
                respond_to_how_are_you()
            elif "time" in command:
                tell_time()
            elif "day" in command:
                tell_day()
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
            elif "open calculator" in command:
                ap.open_calculator()
            elif "open notepad" in command:
                ap.open_notepad()
            elif "search" in command:
                handle_search(command)
            elif "exit" in command or "quit" in command:
                break
            else:
                speak("Sorry, I didn't understand that.")

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")

        except sr.RequestError:
            speak("Sorry, I'm having trouble processing your request.")

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def respond_to_how_are_you():
    response = random.choice(reply_how_are_you_list)
    speak(response)

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    response = f"The current time is {current_time}"
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

# Run the main program
if __name__ == "__main__":
    main()
