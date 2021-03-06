from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_web_driver_options():
    return webdriver.ChromeOptions()

def get_chrome_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--ignore-certificate-errors')
    return webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options = options)

#def get_chrome_web_driver(options):
#    return webdriver.Chrome('./chromedriver', chrome_options = options)

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_automation_as_head_less(option):
    options.add_argument('--headless')
