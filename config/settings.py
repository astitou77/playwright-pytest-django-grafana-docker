"""
Settings module.

Environment variables are expected to be loaded
before importing this module (e.g. by pytest in tests/conftest.py).
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    def __init__(self, env: str):
        # based on the selected env (ste-b, stg, pef...), load the corresponding .env file
        self.dotenv_file = Path(__file__).resolve().parent / "environments" / f"{env}.env"

        # if the .env file does not exist, raise FileNotFoundError
        if not os.path.exists(self.dotenv_file):
            raise FileNotFoundError(f"{self.dotenv_file} file does not exist...")
        
        # Load the environment variables from the .env file
        load_dotenv(dotenv_path=self.dotenv_file)
        print(f"\n\tLoading *.env parameters :\n\t{self.dotenv_file}")

        # Now, set the class attributes from the loaded env. variables
        self.LOG_DIR = os.getenv("LOG_DIR")
        self.ENV = os.getenv("ENV", "ste-b")
        self.BROWSER = os.getenv("BROWSER")
        self.HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
        self.LANGUAGE = os.getenv("LANGUAGE")
        self.URLS = {
            "ETA_PORTAL_URL": os.getenv("ETA_PORTAL_URL"),
            "ETA_STATUS_URL": os.getenv("ETA_STATUS_URL"),
            "PPMI_URL": os.getenv("PPMI_URL"),
            "PPMI_SCAN_SIMULATE_URL": os.getenv("PPMI_SCAN_SIMULATE_URL"),
            "PSS_URL": os.getenv("PSS_URL"),
        }
        self.GCMS_USERS = {
            "GCMS_USER20": os.getenv("GCMS_USER20"),
            "GCMS_USER24": os.getenv("GCMS_USER24"),
        }
        self.GCMS_PASSWORD = os.getenv("GCMS_PASSWORD")  # 3mnaU8JgylAb6f1iRD4Rm99H2Qnmk+Mb6s6uHlq0AEM=

        # Additional env. variables
        self.DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
    
    def __repr__(self):
        return f"<\nEnvironment SETTINGS : \n\tLOG_DIR={self.LOG_DIR} \n\tENV={self.ENV} \n\tBROWSER={self.BROWSER} \n\tHEADLESS={self.HEADLESS}>"

# settings = Settings()

# TEST IT :
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# - - - - - - - - - - - - - - - - - - - - - - - - - -
# print("\nSTART |--- settings.py > Settings(env) ---|\n")

# print("BASE_DIR : ", settings.LOG_DIR)
# print("ENV : ", settings.ENV)
# print("BROWSER : ", settings.BROWSER)
# print("HEADLESS : ", settings.HEADLESS)
# print("LANGUAGE : ", settings.LANGUAGE)
# print("URLS : ", settings.URLS['ETA_PORTAL_URL'])
# print("GCMS_PASSWORD : ", settings.GCMS_PASSWORD)
# print("GCMS_USERS : ", settings.GCMS_USERS['GCMS_USER20'])

# print("\nEND   |--- settings.py > Settings(env) ---|\n")


