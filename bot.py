#need to add to pokemon cards to cart
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--headless=new")
#options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=options)

#setting up chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#Opens up the pokemon card link
driver.get("https://www.target.com/p/2025-pokemon-prismatic-evolutions-accessory-pouch-special-collection/-/A-94300053?clkid=9cdc0658N06ce11f0b1b5b1a9ab1d663c&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002")


wait = WebDriverWait(driver, 60)#waits 3 seconds for the element to load in

def is_in_stock():
    #checks if is item is in stock
    try:
        add_to_cart = driver.find_element(By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")
        if add_to_cart.is_enabled():
            #print("In stock")
            return True
    except:
        time.sleep(2)
        driver.get("https://www.target.com/p/2025-pokemon-hop-39-s-zacian-ex-box/-/A-94484578?clkid=9cdc0658N06ce11f0b1b5b1a9ab1d663c&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002")
        return False
    

def set_quantity():
    quantity_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'select-')]"))).click()
    #look for the 2 quantity option
    quantity_of_two = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='2']"))).click()


def delivery():
    #click on the shipping delivery option
    ship_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-test='fulfillment-cell-shipping']"))).click()

def login():
    #click on the login button
    sign_in_element = wait.until(EC.presence_of_element_located((By.ID, "account-sign-in"))).click()

    sign_in_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-test='accountNav-signIn']"))).click()

    #enter in the email for the target account
    email_input_element = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    email_input_element.clear()
    email_input_element.send_keys("carlos.arias2903@gmail.com")

    #enter in the password for the target account
    password_input_element = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input_element.clear()
    password_input_element.send_keys("Supersoaker1!")

    #click the sign in button
    sign_in_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='login']"))).click()
    #driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_button)

def buy_now():
    buy_now = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Buy now')]"))).click()
    #place the order
    place_order = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Place your order')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", place_order)
    place_order.click()

def set_up_cart():
    #add to cart
    add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, "addToCartButtonOrTextIdFor87450164")))  
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    add_to_cart_button.click()
    #click on view cart and checkout
    view_checkout = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View cart & check out"))).click()


def check_out():
    #click checkout
    try:
        sign_in_checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-test='checkout-button']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_checkout)
        sign_in_checkout.click()
        login()
    except NoSuchElementException:
        checkout_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Check out')]"))).click()

    confirm_address_button = wait.until(EC.presence_of_element_located((By.ID, "radio-b231a5d0-df2b-11ee-b686-a18f1cc8d840"))).click()
    save_and_continue = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Save and continue')]"))).click()
    #click place order
    place_order = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Place your order')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", place_order)
    place_order.click()

def confirm_address():
    confirm_address_button = wait.until(EC.presence_of_element_located((By.ID, "radio-b231a5d0-df2b-11ee-b686-a18f1cc8d840"))).click()
    save_and_continue = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Save and continue')]"))).click()
#some mechanism that waits untill the card is restocked
#keeps the account locked into the browser so we can use buy now.
login()
while True:
    if is_in_stock():
        delivery()
        set_quantity()
        confirm_address()
        buy_now()
        print("Bought sucess")
        break
    


#closes the browser
driver.quit()

