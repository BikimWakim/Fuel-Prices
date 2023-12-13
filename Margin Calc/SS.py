from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time



def get_data():

    current_day = datetime.now().strftime('%d')
    url = f'https://www.supersport.hr/sport/dan/{current_day}/sport/1'
    options = webdriver.ChromeOptions()
    # Add any additional options you need (e.g., headless mode)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10)

    try:
        # Locate the elements containing match information
        match_elements = driver.find_elements(By.CSS_SELECTOR, 'td.ponuda-info.clickable[colspan="6"]')

        for match_element in match_elements:
            print(f"Match info: {match_element.text}")
            # Click on each match to navigate to the detailed view
            match_element.click()
            time.sleep(5)  # Wait for the detailed view to load (adjust as needed)
            # Navigate back to the main page to click on the next match
            driver.back()

    except Exception as e:
        print(f'An error occurred: {str(e)}')

    finally: 
        driver.quit()
get_data()