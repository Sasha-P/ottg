import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys

Chrome, Firefox, Opera = range(3)
WEB_DRIVERS = {
    'dir': 'drivers',
    Chrome: 'chromedriver',
    Firefox: 'geckodriver',
    Opera: 'operadriver'
}

browser_name = Firefox
base_dir = os.path.dirname(os.path.abspath(__file__))
complete_path = os.path.join(base_dir, WEB_DRIVERS['dir'], WEB_DRIVERS[browser_name])

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "/usr/bin/firefox"

browser = webdriver.Firefox(capabilities=caps, executable_path=complete_path)
browser.implicitly_wait(10)
try:
    browser.get('http://localhost:8000')
finally:
    assert 'Django' in browser.title
