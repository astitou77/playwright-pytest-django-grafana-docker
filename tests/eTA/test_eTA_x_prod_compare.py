# import excel *.csv file inputs 1 line at a time
# https://docs.pytest.org/en/7.4.x/how-to/parametrize.html#parametrizing-test-functions
import pytest
from config.settings import settings
import pandas as pd
import os

print(f"Current working directory: {os.getcwd()}")