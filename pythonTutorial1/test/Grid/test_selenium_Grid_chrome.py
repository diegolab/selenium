import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select


def test_1_chrome_pageTitleURL():
    # initialize a chrome driver
    global driver
    rul = 'http://localhost:4444'
    try:
        driver = webdriver.Remote(
            command_executor=rul,
            options=webdriver.ChromeOptions()
        )
        time.sleep(2)
        driver.get('https://www.admlucid.com')
    except:
        print("Could not start browser")
    try:
        assert driver.title == "Home Page - Admlucid"
        assert driver.current_url == "https://www.admlucid.com/"
    except ValueError as e:
        print("Assert Failed "+e.__str__())
    #driver.quit()

def test_2_chrome_submitForm():
    # initialize a chrome driver
    global driver
    rul = 'http://localhost:4444'
    try:
        driver = webdriver.Remote(
            command_executor=rul,
            options=webdriver.ChromeOptions()
        )
        time.sleep(2)
        driver.get('https://www.admlucid.com/Home/WebElements')
    except Exception:
        print("Could not start browser")
    time.sleep(2)
    Name = driver.find_element(by=By.NAME, value="Name")
    Email = driver.find_element(by=By.NAME, value="EMail")
    Phone = driver.find_element(by=By.NAME, value="Telephone")
    Submit = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/form/p[7]/input[1]")
    Name.clear()
    Name.send_keys("John Smith")
    Email.clear()
    Email.send_keys("sjohn@admlucid.com")
    Phone.clear()
    Phone.send_keys("780-889-2889")

    select_element = driver.find_element(by=By.NAME, value="age")
    select = Select(select_element)
    select.select_by_visible_text('12')
    select_element2 = driver.find_element(by=By.NAME, value="Service")
    select = Select(select_element2)
    select.select_by_visible_text('Preschool')

    # scroll to buttom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    Submit.click()
    time.sleep(2)
    driver.switch_to.alert.accept()

    #driver.quit()

@pytest.mark.parametrize("golf", ['Tiger Golf','Golf Vacations','Heritage Pointe Golf Course'])
def test_3_chrome_searchForGolf(golf):
    # initialize a chrome driver
    global driver
    rul = 'http://localhost:4444'
    try:
        driver = webdriver.Remote(
            command_executor=rul,
            options=webdriver.ChromeOptions()
        )
        time.sleep(1)
        driver.get('https://admlucid.com/Golf')
    except:
        print("Could not start browser")
    time.sleep(2)
    searchBox = driver.find_element(by=By.NAME, value="SearchString")
    searchButton = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/table[1]/tbody/tr/td[1]/form/button")

    searchBox.send_keys(golf)
    searchButton.click()

    # driver.quit()
