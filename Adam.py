# main.py

import pyttsx3
import speech_recognition as sr
import random
import datetime
from openpyxl import load_workbook
from applications import open_facebook, open_instagrams, open_google, open_youtube, open_calculator, open_notepad

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
        
        hello_list = [cell.value.lower() for cell in user_sheet['A']]
        how_are_you_list = [cell.value.lower() for cell in user_sheet['B']]
        
        reply_hello_list = [cell.value for cell in replies_sheet['A']]
        reply_how_are_you_list = [cell.value for cell in replies_sheet['B']]
        
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
                hour = datetime.datetime.now().hour
                if 0 <= hour < 12:
                    engine.say("Good morning!")
                elif 12 <= hour < 18:
                    engine.say("Good afternoon!")
                else:
                    engine.say("Good evening!")
                engine.runAndWait()

            elif any(phrase in command for phrase in how_are_you_list):
                engine.say(random.choice(reply_how_are_you_list))
                engine.runAndWait()

            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M")
                engine.say(f"The current time is {current_time}")
                engine.runAndWait()

            elif "day" in command:
                day = datetime.datetime.now().strftime("%A")
                engine.say(f"Today is {day}")
                engine.runAndWait()

            elif "open google" in command:
                open_google()

            elif "open instagram" in command:
                open_instagrams()    

            elif "open youtube" in command:
                open_youtube()

            elif "open facebook" in command:
                open_facebook()

            elif "open calculator" in command:
                open_calculator()

            elif "open notepad" in command:
                open_notepad()

            elif "exit" in command or "quit" in command:
                break

            else:
                engine.say("Sorry, I didn't understand that.")
                engine.runAndWait()

        except sr.UnknownValueError:
            engine.say("Sorry, I couldn't understand what you said.")
            engine.runAndWait()

        except sr.RequestError:
            engine.say("Sorry, I'm having trouble processing your request.")
            engine.runAndWait()

# Run the main program
if __name__ == "__main__":
    main()
