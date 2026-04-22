import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://onlineservices-systest.ci.gc.ca/c2c/launchEapp.do?lang=en&appTypeID=7403")
    page.get_by_label("Problematic field: What would").select_option("7122")
    page.get_by_label("Problematic field: How long").select_option("7348")
    page.get_by_label("Problematic field: Select the").select_option("13287")
    page.get_by_label("Problematic field: What is your current country or territory of residence? If").select_option("1840")
    page.get_by_label("Problematic field: Do you").select_option("997")
    page.get_by_label("Year", exact=True).select_option("975")
    page.get_by_label("Month").select_option("1819")
    page.get_by_label("Day").select_option("548")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Problematic field: What is").select_option("14254")
    page.get_by_role("button", name="Next").click()
    page.get_by_role("link", name="Continue").click()
    page.get_by_label("Problematic field: Which").select_option("2731")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Problematic field: Canada's").select_option("12966")
    page.get_by_role("button", name="Next").click()
    page.get_by_text("Year Select").click()
    page.get_by_label("Year").select_option("4376")
    page.get_by_label("Month").select_option("1819")
    page.get_by_label("Day").select_option("547")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Day").select_option("550")
    page.get_by_label("Year").select_option("4377")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Problematic field: Enter the test score for Speaking. (required)").select_option("17136")
    page.get_by_label("Problematic field: Enter the test score for Listening. (required)").select_option("17137")
    page.locator("[id=\"eapp-question-and-answer-answerlist[3]\"] > .col-md-9").click()
    page.get_by_label("Problematic field: Enter the test score for Reading. (required)").select_option("17136")
    page.get_by_label("Problematic field: Enter the test score for Writing. (required)").select_option("17137")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Problematic field: Do you").select_option("12964")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Problematic field: During").select_option("374246")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Problematic field: In the").select_option("12971")
    page.get_by_role("button", name="Next").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
