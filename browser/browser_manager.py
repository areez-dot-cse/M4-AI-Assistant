from playwright.sync_api import sync_playwright


class BrowserManager:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = None
        self.page = None

    def start_browser(self):
        try:
            # Browser already alive
            if (
                self.browser is not None
                and self.page is not None
            ):
                self.page.title()
                return
        except:
            print("Browser session died. Restarting...")
            self.browser = None
            self.page = None

        self.browser = self.playwright.chromium.launch(
            executable_path=r"C:\Users\areez\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe",
            headless=False
        ) #if headless=true => invisible browser, for automation only
        self.page = self.browser.new_page()
        print("Browser started")


    def open_url(self, url):
        self.start_browser()
        self.page.goto(url)


    def youtube_search(self, query):
        self.start_browser()
        self.page.goto("https://www.youtube.com")
        self.page.wait_for_selector(
            'input[name="search_query"]'
        )
        self.page.fill(
            'input[name="search_query"]',
            query
        )
        self.page.keyboard.press("Enter")


    def play_first_video(self):
        self.start_browser()
        self.page.wait_for_selector(
            "ytd-video-renderer"
        )
        first_video = self.page.locator("ytd-video-renderer a#video-title").first
        first_video.click()


    def get_current_url(self):
        if self.page:
            return self.page.url
        return None


    def get_page_title(self):
        if self.page:
            return self.page.title()
        return None


    def get_page_text(self):
        return self.page.locator("body").inner_text()


    def get_clickable_elements(self):
        elements = self.page.locator("button, a, input[type='submit']")
        count = elements.count()
        results = []
        for i in range(min(count, 20)):
            try:
                text = elements.nth(i).inner_text()  #nth[i] just fetches the element at index i from playwright list, same as elements[i] if it was a simple list
                cleaned = " ".join(text.split())
                if cleaned:
                    results.append(cleaned)
            except:
                pass
        return results


    def click_element(self, selector):
        self.start_browser()
        self.page.wait_for_selector(selector)
        self.page.locator(selector).first.click()


    def type_text(self, selector, text):
        self.start_browser()
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)


    def press_key(self, key):
        self.start_browser()
        self.page.keyboard.press(key)


    def extract_text(self, selector):
        self.start_browser()
        self.page.wait_for_selector(selector)
        return self.page.locator(selector).inner_text()


    def close(self):
        if self.browser:
            self.browser.close()
            self.browser = None
            self.page = None
            print("Browser closed")

browser_manager = BrowserManager()