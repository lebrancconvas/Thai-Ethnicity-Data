from playwright.sync_api import sync_playwright  

BASE_URL = "https://ethnicity.sac.or.th/database-ethnic"

BASE_PATH = "../data/base/markdown"

def get_data_url():
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
    
    browser.close()
    
    return ethnicity_data_url

def save():
  urls = get_data_url()
  output_path = "./output/text/url.txt"

  write_line = ""

  for url in urls:
    write_line += f"{url}\n"

  with open(output_path, "w", encoding="utf-8") as file:
      file.write(write_line)

def get_information():
  with open("./output/text/url.txt", "r", encoding="utf-8") as file:
    urls = file.readlines()
  for url in urls:
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=True)
      context = browser.new_context()
      page = context.new_page() 

      format_url = url.split("\\")[0]
      page.goto(format_url)
      print(f"[LOG] Scraping Data from URL: {format_url}")


def run():
  get_information() 

if __name__ == "__main__":
  run()  