from playwright.sync_api import sync_playwright

BASE_URL = "https://ethnicity.sac.or.th/database-ethnic"

BASE_PATH = "../data/base/markdown"

def run():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()  
    
    print(f"[LOG] Begin to scrape data.")

    page.goto(f"{BASE_URL}")

    # Click More
    MORE_BUTTON_SELECTOR = "body > div.mainPage > div.mainPageContent > div > div > div.overviewGroupList.overflow-hidden > div.overviewGroupListContent > div > div > div.contentListLoadMoreArea.dataListLoadAllArea > button"
    page.click(MORE_BUTTON_SELECTOR)

    page.wait_for_timeout(1500)

    # Get ID
    ETHNIC_LIST_SELECTOR = ".contentListItem > a"  
    result = page.query_selector_all(ETHNIC_LIST_SELECTOR)
    
    # Save Data URL

    ethnicity_data_url = []

    for data in result:
      url = data.get_attribute("href")
      ethnicity_data_url.append(url)
    
    print(ethnicity_data_url)
    print(f"Size of Data: {len(ethnicity_data_url)}")
    return ethnicity_data_url

if __name__ == "__main__":
  run()