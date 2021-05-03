# This program tests the ZehnFunds rewards page for full functionality
# Last Modified 5/3/2021
# Author - Jeffrey Umanzor & Andrew Fallon

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

location = '/Downloads/'

options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=2560x1600")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--verbose')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("prefs", {
    "download.default_directory": location,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': location}}
command_result = driver.execute("send_command", params)
driver.maximize_window()

driver.get("http://juaf.cs.loyola.edu")


def login_error_test():

    username = driver.find_element_by_id("emailInput")
    username.clear()
    username.send_keys("jeff@gmail.com")

    password = driver.find_element_by_id("passwordInput")
    password.clear()
    password.send_keys("wrong password")

    driver.find_element_by_id("login-button").click()

    driver.implicitly_wait(5)

def login_success_test():

    username = driver.find_element_by_id("emailInput")
    username.clear()
    username.send_keys("jeff@gmail.com")

    password = driver.find_element_by_id("passwordInput")
    password.clear()
    password.send_keys("password")

    driver.find_element_by_id("login-button").click()
    driver.implicitly_wait(3)

def sign_out():
    driver.find_element_by_id("sidenavLogout").click()


def redeem_funds_test():
    redeem = driver.find_element_by_id("redeemButton").click()


def profile_page_to_dash():
    profile = driver.find_element_by_id("userName").click()
    driver.find_element_by_id("dashboard-button").click()


def profile_page_to_dash2():
    profile = driver.find_element_by_id("sidenavProfile").click()
    driver.find_element_by_id("sidenavDash").click()




login_error_test()
login_success_test()
profile_page_to_dash()
profile_page_to_dash2()
# redeem_funds_test()
sign_out()

# driver.quit()
