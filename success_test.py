import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qatest.datasub.com/index.html")
    form = page.locator("body > div:nth-child(10) > div > div > div.col-lg-5 > div")
    form.scroll_into_view_if_needed()
    page.get_by_role("textbox", name="Your Name").click()
    page.get_by_role("textbox", name="Your Name").fill("Wiliam")
    page.get_by_role("textbox", name="Your Email").click()
    page.get_by_role("textbox", name="Your Email").fill("wiliam@gmail.com")
    page.locator("#service").select_option("B Service")
    page.get_by_role("textbox", name="Message").click()
    page.get_by_role("textbox", name="Message").fill("kwbqhdvwqvdgj")
    page.get_by_role("button", name="Request A Quote").click()
    success_msg = page.locator("#formStatus")
    expect(success_msg).to_be_visible()
    expect(success_msg).to_have_text("Форма отправлена.")
    time.sleep(2)


    # ---------------------
    context.close()
    browser.close()
    print("ТЕСТ ПРОЙДЕН УСППЕШНО")


with sync_playwright() as playwright:
    run(playwright)
