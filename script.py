import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(website):
    print("launching chrome driver")
    driver_path = '/usr/local/bin/chromedriver'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = '/usr/bin/google-chrome'

    driver = webdriver.Chrome(service = Service(driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded")
        html = driver.page_source
        return html
    finally:
        pass

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    if soup.body:
        return str(soup.body)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content 

def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content[i: i+max_length] for i in range(0, len(dom_content), max_length)
    ]
