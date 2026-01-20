import pytest
from playwright.sync_api import sync_playwright
from config.settings import settings    # env. variables : ENV, LOG_DIR, BROWSER, HEADLESS, URLS, GCMS_USER

# context | session | blahbalh

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = getattr(p, settings.BROWSER).launch(headless=settings.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(base_url=settings.URLS["ETA_PORTAL_URL"])
    page = context.new_page()
    yield page
    context.close()