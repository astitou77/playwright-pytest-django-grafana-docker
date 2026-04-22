import pytest

def test_site_one(page):
    page.goto("https://example.com")
    page.pause()  # pauses here

def test_site_two(page):
    page.goto("https://playwright.dev")
    page.pause()  # pauses here

def test_site_three(page):
    page.goto("https://github.com")
    page.pause()  # pauses here
