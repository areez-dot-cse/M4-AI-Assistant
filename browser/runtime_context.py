from browser.browser_manager import browser_manager


def build_context():
    context = {}
    # Browser context
    try:
        url = browser_manager.get_current_url()
        title = browser_manager.get_page_title()
        context["current_url"] = url
        context["page_title"] = title

    except:
        context["current_url"] = None
        context["page_title"] = None
        
    return context