import pytest
from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://example.com')
        assert page.title() == 'Example Domain'
        page.screenshot(path='reports/screenshot.png')
        browser.close()
