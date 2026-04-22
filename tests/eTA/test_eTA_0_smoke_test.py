import pytest
from config.settings import Settings
import time

def test_simple(function_fixture):
    print("RUN test_simple")
    print("function_fixture : ", function_fixture)
    # print("ENV from settings : ", Settings.LOG_DIR)
# assert function_fixture == "function scope data"

"""
# these are hooks to use when you want to run browser and page setup/teardown at different scopes
@pytest.mark.smoke
@pytest.mark.eTA
def test_login(page):
    page.goto(settings.URLS["ETA_PORTAL_URL"])
    
    time.sleep(999)

    assert page.url.startswith(settings.URLS["ETA_PORTAL_URL"])
"""