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
    intro_content = page.locator(CONTENT_INTRO_SELECTOR).all_text_contents()[0]
    content_body += "\n========= บทนำ =========\n"
    content_body += f"{intro_content}\n"

    CONTENT_BODY_SELECTOR = ".accordion-body"

    # Section 01: ข้อมูลพื้นฐาน
    section_01_content = page.locator(CONTENT_BODY_SELECTOR).all()

    content_body += "\n========= ข้อมูล =========\n" 
    for content in section_01_content:
      content_body += f"{content.inner_text()}\n"

    # Section 02: ประวัติศาสตร์ 
    # SECTION_02_SELECTOR = "#detailSidebar > div > ul > li:nth-child(2)"
    # page.locator(SECTION_02_SELECTOR).click()
    # page.locator("li").get_by_text("ประวัติศาสตร์").click()
    # page.wait_for_timeout(2000)
    # section_02_content = page.locator(CONTENT_BODY_SELECTOR).all_text_contents()[0]
    # content_body += "\n========= ประวัติศาสตร์ =========\n"
    # content_body += f"{section_02_content}\n"

    # # Section 03: การตั้งถิ่นฐานและการกระจายตัว
    # # SECTION_03_SELECTOR = "#detailSidebar > div > ul > li:nth-child(3)"
    # # page.locator(SECTION_03_SELECTOR).click()
    # page.locator("li").get_by_text("การตั้งถิ่นฐานและกระจายตัว").click()
    # page.wait_for_timeout(2000)
    # section_03_content = page.locator(CONTENT_BODY_SELECTOR).all_text_contents()[0]
    # content_body += "\n========= การตั้งถิ่นฐานและการขยายตัว =========\n"
    # content_body += f"{section_03_content}\n"

    # # Section 04: วิถีชีวิตและวัฒนธรรม
    # # SECTION_04_SELECTOR = "#detailSidebar > div > ul > li:nth-child(4)"
    # # page.locator(SECTION_04_SELECTOR).click()
    # page.locator("li").get_by_text("วิถีชีวิตและวัฒนธรรม").click()
    # page.wait_for_timeout(2000)
    # section_04_content = page.locator(CONTENT_BODY_SELECTOR).all_text_contents()[0]
    # content_body += "\n========= วิถีชีวิตและวัฒนธรรม =========\n"
    # content_body += f"{section_04_content}\n"

    # # Section 05: งานวิจัยที่เกี่ยวข้อง
    # # SECTION_05_SELECTOR = "#detailSidebar > div > ul > li:nth-child(5)"
    # # page.locator(SECTION_05_SELECTOR).click()
    # page.locator("li").get_by_text("งานวิจัยที่เกี่ยวข้อง").click()
    # page.wait_for_timeout(2000)
    # section_05_content = page.locator(CONTENT_BODY_SELECTOR).all_text_contents()[0]
    # content_body += "\n========= งานวิจัยที่เกี่ยวข้อง =========\n"
    # content_body += f"{section_05_content}\n"

    # Section 06: อ้างอิง  
    # SECTION_06_SELECTOR = "#detailSidebar > div > ul > li:nth-child(6)"
    # page.locator(SECTION_06_SELECTOR).click()
    # page.locator("li").get_by_text("อ้างอิง").click()  
    # page.wait_for_timeout(2000)
    # section_06_content = page.locator(CONTENT_BODY_SELECTOR).all_text_contents()[0]
    # content_body += "\n========= อ้างอิง =========\n"
    # content_body += f"{section_06_content}\n"

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