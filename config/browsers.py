from playwright.sync_api import BrowserType, Playwright
from config.settings import settings                            # BROWSER, HEADLESS

def get_browser(playwright: Playwright) -> BrowserType:
    if settings.BROWSER == "chromium":
        return playwright.chromium
    if settings.BROWSER == "firefox":
        return playwright.firefox
    if settings.BROWSER == "webkit":
        return playwright.webkit
    raise ValueError(f"Unsupported Browser: {settings.BROWSER}")

def browser_launch_options():
    return {
        "headless": settings.HEADLESS,
        "slow_mo": 0,
    }