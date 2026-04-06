from playwright.sync_api import sync_playwright

BASE_URL = "https://ethnicity.sac.or.th/database-ethnic"

BASE_PATH = "../data/base/markdown"

def run():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(f"{BASE_URL}")

    # Click More
    MORE_BUTTON = page.get_by_text("ดูทั้งหมด")
    page.click("body > div.mainPage > div.mainPageContent > div > div > div.overviewGroupList.overflow-hidden > div.overviewGroupListContent > div > div > div.contentListLoadMoreArea.dataListLoadAllArea > button")

    # Get ID
    ETHNIC_LIST = "ethnicList"
    result = page.locator(ETHNIC_LIST).get_attribute("href") 
    print(result)  

if __name__ == "__main__":
  run()