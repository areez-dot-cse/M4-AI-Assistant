from browser.browser_manager import browser_manager


def open_website(url):
    browser_manager.open_url(url)
    return f"Opened {url}"


def youtube_search(query):
    browser_manager.youtube_search(query)
    return f"Searched YouTube for {query}"


def play_first_video():
    browser_manager.play_first_video()
    return "Playing first video"


def close_browser():
    browser_manager.close()
    return "Browser closed"


def current_website():
    url = browser_manager.get_current_url()
    if url:
        return f"Current website is {url}"
    return "No active browser page"


def current_page_title():
    title = browser_manager.get_page_title()
    if title:
        return f"Current page title is {title}"
    return "No active page"


def click_element(selector):
    browser_manager.click_element(selector)
    return f"Clicked element {selector}"


def type_text(selector, text):
    browser_manager.type_text(selector, text)
    return f"Typed text into {selector}"


def press_key(key):
    browser_manager.press_key(key)
    return f"Pressed {key}"


def extract_text(selector):
    text = browser_manager.extract_text(selector)
    return text


def get_page_text():
    text = browser_manager.get_page_text()
    return text[:3000]


def get_clickable_elements():
    elements = browser_manager.get_clickable_elements()
    return str(elements)