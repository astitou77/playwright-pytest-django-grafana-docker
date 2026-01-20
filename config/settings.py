import os
from pathlib import Path
from dotenv import load_dotenv


# If the *.env file exists, load all its env. variables to current context
BASE_DIR = Path(__file__).resolve().parent
env_file = BASE_DIR / "environments" / "ste-b.env"
if env_file.exists():
    load_dotenv(env_file)


# Environment Variables 
# From : "../Playwright/config/environments/*.env"

class Settings:
    LOG_DIR = os.getenv("LOG_DIR")

    ENV = os.getenv("ENV", "ste-b")

    BROWSER = os.getenv("BROWSER")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    LANGUAGE = os.getenv("LANGUAGE")

    URLS = {
        "ETA_PORTAL_URL": os.getenv("ETA_PORTAL_URL"),
        "ETA_STATUS_URL": os.getenv("ETA_STATUS_URL"),
        "PPMI_URL": os.getenv("PPMI_URL"),
        "PPMI_SCAN_SIMULATE_URL": os.getenv("PPMI_SCAN_SIMULATE_URL"),
        "PSS_URL": os.getenv("PSS_URL"),
    }

    GCMS_USERS = {
        "GCMS_USER20": os.getenv("GCMS_USER20"),
        "GCMS_USER24": os.getenv("GCMS_USER24"),
    }

    GCMS_PASSWORD = os.getenv("GCMS_PASSWORD")  # 3mnaU8JgylAb6f1iRD4Rm99H2Qnmk+Mb6s6uHlq0AEM=

    # Additional env. variables
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))

settings = Settings()

# TEST IT :
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# - - - - - - - - - - - - - - - - - - - - - - - - - -
print("BASE_DIR : ", settings.LOG_DIR)
print("ENV : ", settings.ENV)
print("BROWSER : ", settings.BROWSER)
print("HEADLESS : ", settings.HEADLESS)
print("LANGUAGE : ", settings.LANGUAGE)
print("URLS : ", settings.URLS['ETA_PORTAL_URL'])
print("GCMS_PASSWORD : ", settings.GCMS_PASSWORD)
print("GCMS_USERS : ", settings.GCMS_USERS['GCMS_USER20'])


