from playwright.sync_api import BrowserType, Playwright
from config.settings import settings # env. vars : BROWSER, HEADLESS

def get_browser(playwright: Playwright) -> BrowserType:
    if BROWSER== "chromium":
        return playwright.chromium
    if BROWSER== "firefox":
        return playwright.firefox
    if BROWSER== "webkit":
        return playwright.webkit
    raise ValueError(f"Unsupported Browser: {BROWSER}")

def browser_launch_options():
    return {
        "headless": HEADLESS,
        "slow_mo": 0,
    }