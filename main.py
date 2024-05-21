import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
import pytesseract
from PIL import Image

def print_header():
    print(Fore.BLUE + "         Shopee LiveBot BY.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   ")
    print(Fore.BLUE + "         ██████|||███████████|||████████|||████  ████||||██||||||██   ")
    print(Fore.GREEN + "         ██  ██   ██   ██  ██   ██    ██    ██    ██     ██ ██   ██   ")
    print(Fore.RED + "         ██████   ██   ██  ██   ████████    ██    ██     ██  ██  ██   ")
    print(Fore.YELLOW + "         ██  ██   ██   ██  ██   ██   ██     ████████     ██    ████   ")
    print(Style.RESET_ALL + "         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.Dev  ")
    print(Fore.BLUE + "         ")

def setup_selenium(proxy_address=None):
    # Set path to Chrome WebDriver
    chrome_driver_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'

    # Configure Chrome options
    options = webdriver.ChromeOptions()
  
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
  
    # Add proxy settings if provided
    if proxy_address:
        options.add_argument(f'--proxy-server={proxy_address}')

    # Specify the Chrome WebDriver executable path using Service
    service = Service(executable_path=chrome_driver_path)

    # Launch browser
    browser = webdriver.Chrome(service=service, options=options)
    # Clear cache and cookies
    browser.delete_all_cookies()
    return browser

def solve_text_captcha(browser, captcha_element):
    try:
        # Ambil screenshot dari captcha
        screenshot_path = 'captcha_screenshot.png'
        captcha_element.screenshot(screenshot_path)
        
        # Gunakan OCR untuk mengenali teks dari gambar captcha
        captcha_text = pytesseract.image_to_string(screenshot_path)
        
        # Hapus file screenshot setelah selesai
        os.remove(screenshot_path)
        
        return captcha_text
    except Exception as e:
        print("Failed to solve CAPTCHA:", e)
        return None

def input_data():
    try:
        global loop_count, session_id, viewer
        # Prompt user for session ID
        session_id = input('(#) Session ID : ')
        # Prompt user for viewer
        viewer = input('(#) Trends : ')
        # Prompt user for the number of times to loop
        loop_count = int(input('(#) Jumlah Viewers: '))
        if loop_count <= 0:
            raise ValueError("Number of viewers should be a positive integer.")
        viewers = random.randint(1, 100)
        link_live = f"https://live.shopee.co.id/share?from=live&session={session_id}&stm_medium=referral&stm_source=rw&viewer={viewers}"
        return loop_count, link_live
    except ValueError as ve:
        print("Invalid input:", ve)
        return input_data()

def navigate_to_link(browser, link):
    try:
        browser.get(link)
    except Exception as e:
        print("An error occurred while navigating to the link:", e)

def click_element(browser, selector, success_message=None):
    try:
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
        element.click()
        if success_message:
            print(success_message)
    except Exception as e:
        print("An error occurred while clicking the element:", e)

print_header()
loop_count, link_live = input_data()
# proxy_address = '157.66.54.6:1034'  # Proxy address provided by you
browser = setup_selenium()
wait = WebDriverWait(browser, 10)

# Loop to add viewers
for _ in range(loop_count):
    navigate_to_link(browser, 'https://shopee.co.id/buyer/login/qr')
    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.shopee-avatar__img')))
    
    navigate_to_link(browser, link_live)
    click_element(browser, '//*[@id="__next"]/div/div[2]/div[1]/div', "Viewers added successfully!")

