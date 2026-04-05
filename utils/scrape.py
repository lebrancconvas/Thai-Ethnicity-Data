from playwright.sync_api import sync_playwright

BASE_URL = "https://ethnicity.sac.or.th/database-ethnic"

BASE_PATH = "../data/base/markdown"

def run():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(f"{BASE_URL}")


if __name__ == "__main__":
  run()