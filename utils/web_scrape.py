from playwright.sync_api import sync_playwright  

LOCALE = "en-US"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"

BASE_URL = "https://ethnicity.sac.or.th/database-ethnic"
BASE_PATH = "./data/knowledge/markdown"

def get_data_urls():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(locale=LOCALE, user_agent=USER_AGENT)
    page = context.new_page()

    page.goto(BASE_URL)

    MORE_BUTTON_SELECTOR = ".btn-loadMore"
    LIST_OF_DATA_SELECTOR = ".contentListItem"

    more_button = page.locator(MORE_BUTTON_SELECTOR)
    more_button.click()

    page.wait_for_timeout(1500)

    data_list = page.locator(LIST_OF_DATA_SELECTOR).all()

    data_urls = []
    
    for index, data in enumerate(data_list):
      url = data.locator("a").get_attribute("href")
      data_urls.append(url)

  return data_urls  

def get_data(url: str):
  content_body = ""
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(locale=LOCALE, user_agent=USER_AGENT)
    page = context.new_page()

    page.goto(url)

    # Intro
    TITLE = page.title()
    ID = url.split("/")[-2]
    FILE_NAME = f"{ID}_{"_".join(TITLE.split(" "))}"

    content_body += f"ID: {ID}\nTitle: {TITLE}\n"

    CONTENT_INTRO_SELECTOR = ".pageDetailIntro"
    intro_content = page.locator(CONTENT_INTRO_SELECTOR).inner_text()  
    content_body += "\n========= บทนำ =========\n"
    content_body += f"{intro_content.strip()}\n"

    CONTENT_BODY_SELECTOR = ".accordion-body"

    main_content = page.locator(CONTENT_BODY_SELECTOR).all()

    content_body += "\n========= ข้อมูล =========\n" 
    for content in main_content:
      content_body += f"{content.inner_text().strip()}\n"

    with open(f"./data/knowledge/text/web_information/{FILE_NAME}.txt", "w", encoding="utf-8") as f:
      f.write(content_body)
  return content_body 

def run():
  urls = get_data_urls()

  for url in urls:
    # test_data_url = "https://ethnicity.sac.or.th/database-ethnic/156/"
    result = get_data(url)
    print(f"[LOG] Success: Get Data from URL: {url} success.")

if __name__ == "__main__":
  run()