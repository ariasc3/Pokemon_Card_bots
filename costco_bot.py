#need to add to pokemon cards to cart
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

#sign into the google profile

#profile_path = r"C:\Users\Carlo\AppData\Local\Google\Chrome\User Data"

#options = webdriver.ChromeOptions()
#options.add_argument("--disable-build-check")
#options.add_argument(f"user-data-dir={profile_path}")
#options.add_argument("profile-directory=Profile 4")
#options.add_argument("--incognito")

#setting up chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Opens up the pokemon card link
driver.get("https://www.costco.com/pokemon-3-pack-paldea-partners-tins.product.4000352232.html")


wait = WebDriverWait(driver, 60)#waits 3 seconds for the element to load in

time.sleep(60)
#close browser
driver.quit()