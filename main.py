import speech_recognition as sr
import sys

from core.validator import validate_plan
from system.voice import speak
from core.router import classify_intent
from ai.chat import chat_response
from core.planner import generate_plan
from core.executor import execute_plan
from browser.browser_manager import browser_manager


wakeword = "m4"

r = sr.Recognizer()


def listen(timeout=2, phrase_time_limit=5):

    with sr.Microphone() as source:

        print("\nListening...")

        audio = r.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )

    print("Recognizing...")

    try:

        return r.recognize_google(audio)

    except:

        return ""


def processCommand(command):

    command = command.lower()
    intent = classify_intent(command)

    # Shutdown
    if "shutdown assistant" in command:

        speak("Shutting down")

        browser_manager.close()

        sys.exit()


    try:
        # Conversational requests
        if intent == "CHAT":
            response = chat_response(command)
            print("\nCHAT RESPONSE:\n")
            print(response)
            speak(response)
            return "chat"

        # Generate execution plan
        plan = generate_plan(command)

        # Validate plan
        valid, message = validate_plan(plan)

        if not valid:

            speak("Invalid execution plan")

            print(message)

            return "error"


        # Empty plan
        if len(plan["steps"]) == 0:

            speak("I cannot perform that action yet")

            return "error"


        print("\nGENERATED PLAN:\n")
        print(plan)


        # Execute plan
        results = execute_plan(plan)


        print("\nEXECUTION RESULTS:\n")
        for result in results:
            print("-", result)

        important_results = []
        for result in results:
            lowered = result.lower()
            # Skip noisy browser narration
            if (
                "opened" in lowered
                or "searching google" in lowered
                or "searched youtube" in lowered
                or "playing first video" in lowered
                or "opening chrome" in lowered
            ):
                continue
            # Skip clickable elements dumps
            if lowered.startswith("['"):
                continue
            important_results.append(result)

        # Speak filtered responses
        for result in important_results:
            speak(result)

    except Exception as e:

        print(f"\nERROR:\n{e}")

        speak("Something went wrong")

        return "error"


if __name__ == "__main__":

    print("M416 INITIALIZED")

    speak("Initializing M4")

    while True:

        try:

            # Wake-word listening
            word = listen(
                timeout=2,
                phrase_time_limit=2
            )

            if not word:
                continue

            print(f"user: {word}")

            if wakeword in word.lower():

                speak("Yes sir")

                # Command mode
                command = listen(
                    timeout=5,
                    phrase_time_limit=10
                )

                if not command:

                    speak("I did not hear anything")

                    continue

                print(f"user: {command}")

                status = processCommand(command)


        except sr.WaitTimeoutError:

            continue


        except Exception as e:

            print(f"\nERROR:\n{e}")