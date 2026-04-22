import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# ---- Test Data Source (equivalent to TRCloudData.TRVSmokeData) ----
def trv_smoke_data():
    return [
        {"email": "client@example.com", "role": "client"},
        {"email": "paidrep@example.com", "role": "paid_rep"}
    ]


# ---- Test Class Equivalent ----
class TestTRCloudTRVSmoke:

    @pytest.fixture
    def driver(self):
        options = Options()
        options.add_argument("--headless")
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)
        yield driver
        driver.quit()

    @pytest.mark.parametrize("comboParamsDict", trv_smoke_data())
    def test_TRCloudTRV(self, driver, comboParamsDict):
        """
        Precondition:
        TRV Cloud Smoke test is split into two tests (Client login and Paid Rep login).
        For first-time runs or after STG refresh, valid emails are required to create
        or validate accounts—especially the Paid Rep account.

        Account creation instructions:
        - TR eApps account creation instructions: T:\Automation_Team\Training\TrainingVideo\TRCloud
        - All URLs: "All URLs of TR Cloud Test.doc"
        - Paid Rep account creation: "REP PORTAL DEMO-20230926_141330-Meeting Recording"
        - AD account for approval must have "Party Admin" roles
        - Client account creation: "How to sign up a new account for TR Cloud login test in STG"
        """

        # Example usage of the test data
        email = comboParamsDict.get("email")
        role = comboParamsDict.get("role")

        print(f"Running smoke test for role: {role}, email: {email}")

        # Example Selenium action
        driver.get("https://example.com/login")

        # You would continue with:
        # - entering email
        # - clicking login
        # - validating dashboard
        # etc.
