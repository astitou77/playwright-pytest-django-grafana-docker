"""
1 - Command-line parsing
2 - Load plugins
3 - Load conftest.py files
4 - Test discovery
    4.1 - Directories (alphabetical)
    4.2 - Files (alphabetical)
    4.3 - Classes (alphabetical)
    4.4 - Functions (alphabetical)
    4.5 - Methods (alphabetical)
    4.6 - Parameters (as defined)
    4.7 - Marks (as defined)
    4.8 - Fixtures (as defined)
    * Note: Steps 4.1 to 4.8 are interleaved during discovery
    * You can enforece order using pytest-order plugin
    * pytest-order plugin: https://pypi.org/project/pytest-order/
    * pytest-dependencies plugin: https://pypi.org/project/pytest-dependencies/
    * -k select by substring expression
    * -m select by mark expression
    * Explicit node IDs are always run first

5 - Fixture resolution

    5.1 setup session fixtures
        5.2 setup package fixtures
            5.3 setup module fixtures
                5.4 setup class fixtures
                    5.5 setup function fixtures (a → b → c)
                    RUN TEST
                    5.6 teardown function fixtures (c → b → a)
            5.7 teardown class fixtures
        5.8 teardown module fixtures
    5.9 teardown package fixtures
    5.10 teardown session fixtures

6 - Test execution
7 - Teardown
8 - Reporting
"""

# context | session | blahbalh

# pytest fixture SCOPE reference: https://docs.pytest.org/en/7.4.x/how-to/fixtures.html#fixture-scopes
# 1. session: invoked once per test session
# 2. package: invoked once per package
# 3. module: invoked once per module
# 4. class: invoked once per test class
# 5. function: default, invoked per test function

import os
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
# env. variables : ENV, LOG_DIR, BROWSER, HEADLESS, URLS, GCMS_USER, etc.
from config.settings import Settings

# pytest hook to add command-line options ; ex.: pytest --env=stg
def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store", 
        default="ste-b", 
        help="Environment to run tests against : [ ste-b ] or [ stg ]"
    )

# pytest hook to configure settings before tests run
def pytest_configure(config):
    print("\nSTART |--- conftest.py > pytest_configure(config) ---|\n")

    env = config.getoption("--env")
    print(f"\tSelected Environment: [ {env} ] ")

    BASE_DIR = Path(__file__).resolve().parent.parent
    dotenv_file = BASE_DIR / "config" / "environments" / f"{env}.env"
    if not os.path.exists(dotenv_file):
        raise FileNotFoundError(f"{dotenv_file} file does not exist...")
    
    # Load from [ ste-b | stg ].env : LOG_DIR, ENV, BROWSER, HEADLESS, URLS, GCMS_USER, etc.
    load_dotenv(dotenv_path=dotenv_file, override=True)
    print(f"\n\tLoading *.env parameters :\n\t{dotenv_file}")

    # Now, settings can be accessed in tests via : 'from config.settings import Settings'

    # CI/CD pipelines can pass 'pytest --env=stg' to run tests against staging env.
    # or override env. variables directly in the pipeline

    print("\nEND   |--- conftest.py > pytest_configure(config) ---|\n")

# Instantiate settings after loading the .env file
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = getattr(p, Settings.BROWSER).launch(headless=Settings.HEADLESS)
        yield browser
        browser.close()

# Define a page fixture that uses the browser fixture
@pytest.fixture
def page(browser):
    context = browser.new_context(base_url=settings.URLS["ETA_PORTAL_URL"])
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(autouse=True)
def trace_on_failure(page, request):
    yield
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png")


# Define pytest fixtures with different scopes

# pytest fixture autouse reference: https://docs.pytest.org/en/7.4.x/how-to/fixtures.html#autouse-fixtures
#   autouse=True : fixture is automatically used by tests without needing to declare it explicitly
#   autouse=False: fixture must be explicitly declared in test functions or classes to be used

@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("\n--- Setup session_fixture ---")
    yield "SESSION !!!!!!!!!!!!!!!!!"
    print("\n--- Teardown session_fixture ---")

@pytest.fixture(scope="package", autouse=True)
def package_fixture():
    print("\n--- Setup package_fixture ---")
    yield "PACKAGE !!!!!!!!!!!!!!!!!"
    print("\n--- Teardown package_fixture ---")

@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    print("\n--- Setup module_fixture ---")
    yield "MODULE !!!!!!!!!!!!!!!!!"
    print("\n--- Teardown module_fixture ---")

@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("\n--- Setup class_fixture ---")
    yield "CLASS !!!!!!!!!!!!!!!!!"
    print("\n--- Teardown class_fixture ---")

@pytest.fixture(scope="function")
def function_fixture():
    print("\n--- Setup function_fixture ---")
    yield "FUNCTION !!!!!!!!!!!!!!!!!"
    print("\n--- Teardown function_fixture ---")



"""



"""