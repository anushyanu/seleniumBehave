import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch the browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('open Orangehrm home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(10)

@then('verify that the logo present on home page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-branding']").is_displayed()
    time.sleep(5)
    assert status is True

@then('close the browser')
def closeBrowser(context):
    context.driver.close()