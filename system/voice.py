import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print(f"\nM416: {text}")
    speaker.Speak(text)