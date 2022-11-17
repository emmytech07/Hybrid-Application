from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import By, AppiumBy
import time as sl
desired_caps = dict(
    deviceName='Andriod',
    platformName='Android',
    appPackage='com.android.chrome',
    appActivity='org.chromium.chrome.browser.ChromeTabbedActivity',

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.get('http://google.com')
sl.sleep(2)
# contexts = driver.contexts
#
# for context in contexts:
#     print(context)
#
# driver.switch_to.context('WEBVIEW_chrome')

webview = driver.contexts[1]

driver.switch_to.context(webview)

driver.find_element(By.XPATH, "//*[@name='q']").send_keys("Hello Appium !!!")

sl.sleep(2)
driver.quit()