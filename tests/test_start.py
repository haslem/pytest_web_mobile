import test_web_mobile
import mobile_web

import pytest
import json
from appium import webdriver
#from selenium import webdriver as web_driver
from selenium.webdriver import Chrome



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
        # chrome_options = web_driver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # driver = Chrome(options=chrome_options)
        driver.maximize_window()
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-infobars")
# # chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)



# def test_folder_sync_web_mobile(browser, mobile):
#     test_web_mobile.test_folder_sync(browser, mobile)
#
# def test_folder_sync_mobile_web(browser, mobile):
#     mobile_web.test_mobile_web_folder_sync(browser, mobile)

def test_folder_sync(browser, mobile):
    test_web_mobile.test_folder_sync(browser, mobile)

def test_poi_changed_name(browser, mobile):
    test_web_mobile.test_poi_changed_name(browser, mobile)

def test_base_poi(browser, mobile):
    test_web_mobile.test_base_poi(browser, mobile)
#
# def test_firm_poi(browser, mobile):
#     test_web_mobile.test_firm_poi(browser, mobile)
#
# def test_pubt_poi(browser, mobile):
#     test_web_mobile.test_pubt_poi(browser, mobile)
#
# def test_osm_poi(browser, mobile):
#     test_web_mobile.test_osm_poi(browser, mobile)
#
# def test_country_poi(browser, mobile):
#     test_web_mobile.test_country_poi(browser, mobile)
#
# def test_muni_poi(browser, mobile):
#     test_web_mobile.test_muni_poi(browser, mobile)
#
# def test_coor_changed_name(browser, mobile):
#     test_web_mobile.test_coor_changed_name(browser, mobile)
#
# def test_coor_changed_name_rename(browser, mobile):
#     test_web_mobile.test_coor_changed_name_rename(browser, mobile)
#
# def test(browser, mobile):
#     test_web_mobile.test_planning(browser, mobile)