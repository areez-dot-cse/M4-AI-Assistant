import speech_recognition as sr
from voice import speak
from intent import parse_intent
from chat import generate_chat_response
from tools import *
from memo import *
import sys

wakeword = "m4"
r = sr.Recognizer()


def listen(timeout=2, phrase_time_limit=4):
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )
    print("Recognizing...")
    return r.recognize_google(audio)


def processCommand(command):
    command=command.lower()
    if "shutdown assistant" in command:
        response = "Shutting down"
        speak(response)
        sys.exit()
   
    try:
        intent = parse_intent(command)
        if intent["type"] == "chat":
            response = generate_chat_response(command)
            print("\nCHAT RESPONSE:\n")
            print(response)

        elif intent["type"] == "tool":
            action = intent["action"]
            parameters = intent["parameters"]

            if action == "open_app":
                response = open_app(
                    parameters["app_name"]
                )
            elif action == "get_datetime":
                response = get_datetime(
                    parameters["kind"]
                )
            elif action == "remember_item":
                response = remember(
                    parameters["thing"],
                    parameters["place"]
                )
            elif action == "recall_item":

                response = recall(
                    parameters["thing"]
                )
            else:
                response = "Unknown action"

        else:
            response = "Invalid intent"

    except Exception as e:

        response = f"Error: {e}"

    print(response)
    speak(response)


if __name__ == "__main__":
    speak("Initializing M4")

    while True:

        try:
            # Wake-word mode
            word = listen(
                timeout=2,
                phrase_time_limit=2
            )
            print(word)

            if wakeword in word.lower():
                print(f"{wakeword} Active")
                speak("Yes Sir")
                try: 
                # Command mode
                    command = listen(
                        timeout=10,
                        phrase_time_limit=12
                    )
                    print(command)
                    processCommand(command)
                except Exception as e:
                 speak("Back 2 standby.")
        except Exception as e:
            print(e)
    