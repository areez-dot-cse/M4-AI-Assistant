import os
import pyautogui
from datetime import datetime
from browser.browser_manager import browser_manager

def open_app(app_name):
    act = f"Opening {app_name}"
    match app_name.lower():
        case "chrome":
            os.system("start chrome")
        case "whatsapp":
            os.system("start whatsapp")
        case "telegram":
            os.system("start telegram")
        case "youtube":
            os.system('start brave "https://www.youtube.com"')
        case "google":
            os.system('start brave "https://www.google.com"')
        case "vscode":
            os.system("code")
        case "notepad":
            os.system("notepad")
        case _:
            os.system(f'start brave "https://www.google.com/search?q={app_name}"')
            act = f"Cant Find {app_name}, Searching on Web"
    return act


def get_datetime(kind):
    now = datetime.now()
    if kind == "date":
        act = f"The date is {now.date()}"
    elif kind == "time":
        current_time = now.strftime("%I:%M %p")
        act = f"The time is {current_time}"
    else:
        act = "Invalid datetime request"
    return act


def web_search(query):
    browser_manager.open_url(
        f"https://www.google.com/search?q={query}"
    )
    return f"Searching Google for {query}"


def increase_volume():                    #set_max/min_volume, how much to inc/dec
    pyautogui.press("volumeup")
    return "Volume increased"


def decrease_volume():
    pyautogui.press("volumedown")
    return "Volume decreased"


def play_pause_media():
    pyautogui.press("space")
    return "Toggled media playback"