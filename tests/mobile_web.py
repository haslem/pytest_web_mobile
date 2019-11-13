from appium import webdriver

from screens.main_screen import MainScreen
from screens.menu_screen import MenuScreen
from screens.login_screen import LogInScreen
from screens.my_maps_screen import MyMapsScreen

import json
import pytest

from selenium.webdriver import Chrome

from pages.first import FirstPage
from pages.search_page import SearchPage
from pages.my_maps_page import MyMapsPage
from pages.login_page import LoginPage
from pages.save_page import SavePage

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='session')
def desired_cap():
    with open('desired_cap.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def mobile(desired_cap):
    desired_cap = desired_cap

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def config():
    with open('config_web.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def browser(config):
    if config['browser'] == 'chrome':
        driver = Chrome()
        driver.maximize_window()
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_mobile_web_folder_sync(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu = MenuScreen(mobile)
    menu.places_and_routes()

    my_maps = MyMapsScreen(mobile)
    my_maps.create_folder()


    #web check
    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    login = LoginPage(browser)
    login.sign_in()

    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    my_maps = MyMapsPage(browser)

    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/h2")))
    assert elem.text == 'Changed names'


    #delete folder
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/span[2]').click()
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/ul/li[4]').click()

    elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()
