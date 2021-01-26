from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

selenium_grid_ip = 'selenium-hub'

chrome = webdriver.Remote(
          command_executor='http://{}:4444/wd/hub'.format(selenium_grid_ip),
          desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
          command_executor='http://{}:4444/wd/hub'.format(selenium_grid_ip),
          desired_capabilities=DesiredCapabilities.FIREFOX) 

chrome.get('https://www.google.com')
print(chrome.title)

firefox.get('https://www.google.com')
print(firefox.title)

firefox.get('https://dbeaver.io/')
dbeaver_version = firefox.find_element_by_xpath('//*[@id="wdg_specialrecentpostsfree-3-srp-singlepost-1"]/div/div/h4/a').text
print("dveaver version: {}".format(str(dbeaver_version.split()[1])))

chrome.quit()
firefox.quit()