import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from fake_useragent import UserAgent

@pytest.fixture(scope="module")
def driver():
    # Setup Chrome driver
    options = Options()
    options.add_argument('--user-data-dir=/path/to/your/custom/profile')
    chrome_options = Options()
    time.sleep(5)
    chrome_options.add_argument("--start-maximized")
    options.add_argument("disable-infobars")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)  # Use uc.Chrome here

    yield driver

    # Teardown
    driver.quit()

# @pytest.fixture(scope="module")
# def driver():
#     # Setup Chrome driver with undetected_chromedriver and fake_useragent
#     options = Options()
    
#     # Generate a random user agent
#     ua = UserAgent()
#     random_user_agent = ua.random
#     options.add_argument(f'user-agent={random_user_agent}')
    
#     # Optional: Use a custom user data directory
#     # options.add_argument('--user-data-dir=/path/to/your/custom/profile')
    
#     # Additional Chrome options
#     options.add_argument("--start-maximized")
#     options.add_argument("disable-infobars")
    
    # # Setup ChromeDriver service
    # service = Service(ChromeDriverManager().install())
    
    # # Initialize the driver with undetected_chromedriver and the configured options
    # driver = uc.Chrome(service=service, options=options)
    
    # yield driver

    # # Teardown
    # driver.quit()


@pytest.mark.skip(reason="BLOCKED :Human verification on site is detecting the bot automation software")
def test_delivery_quotation(driver):
    time.sleep(5)
    driver.get('https://my.cargoboard.com/')
    time.sleep(5)
    
    consent_element = driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    consent_element.click()

    collection_location = driver.find_element(By.ID, "locations_pickUpLocation")
    collection_location.send_keys('10117')
    #collection_location.click()

   # time.sleep(10)

    delivery_location = driver.find_element(By.ID, "locations_deliveryLocation").send_keys("33100 Paderborn, DE")
    #delivery_location.send_keys('33100 Paderborn, DE')
    #delivery_location.click()

    Random = driver.find_element(By.XPATH, "//*[@id='bulky_goods']/div/div/form/div[3]/div[2]/div/div[1]")
    Random.click()
    time.sleep(15)
    # human = verification.find_element(By.XPATH, "//*[@id='challenge-stage']/div/label/input")
    # human.click()
    time.sleep(10)
    
    Calculate_price = driver.find_element(By.XPATH, '//*[@id="bulky_goods"]/div/div/div/div/button')
    Calculate_price.click()
    time.sleep(5)
    # Add assertions or additional steps here as needed

