from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'Iphone'
CURRENCY = 'Rs'
MIN_PRICE = '30000'
MAX_PRICE = '45000'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.in/"


def get_chrome_web_driver(options):
    return webdriver.Chrome("chromedriver.exe", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')
