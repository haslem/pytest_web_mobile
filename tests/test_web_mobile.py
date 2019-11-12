import json
import pytest
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


# def test_menu_button(mobile):
#     main_screen = MainScreen(mobile)
#     main_screen.menu_click()
#
#
# def test_offlinemaps_button(mobile):
#     main_screen = MainScreen(mobile)
#     main_screen.menu_click()
#
#     menu_screen = MenuScreen(mobile)
#     menu_screen.offline_maps()
#
#
#
#
#
#
# def test_mapy_search(browser):
#     SEARCH = 'Dresden'
#
#     search = FirstPage(browser)
#     search.load()
#     search.search(SEARCH)
#
#     search_result = SearchPage(browser)
#     assert search_result.search_result() == 'Dresden'
#
#
# def test_mapy_change(browser):
# 	change = FirstPage(browser)
# 	change.load()
#
#
# 	change.change_map_historic()
#
#
# 	#open change map menu and ckeck if historic is active
# 	change.change_map()
# 	assert browser.find_element(By.CSS_SELECTOR, "li[class='19stoleti active']")
#
#
#
#
#
#
#
#
# def test_login(mobile):
#     USER_NAME = 'mapytesting2'
#     PASSWORD = 'testingmapy'
#
#     main_screen = MainScreen(mobile)
#     main_screen.menu_click()
#
#     menu_screen = MenuScreen(mobile)
#     menu_screen.log_in()
#
#     login_screen = LogInScreen(mobile)
#     login_screen.user_name(USER_NAME)
#     login_screen.password(PASSWORD)
#     login_screen.sign_in_button()
#
#     user_name = mobile.find_element_by_id('cz.seznam.mapy:id/userName').get_attribute('text')
#     password = mobile.find_element_by_id('cz.seznam.mapy:id/accountName').get_attribute('text')
#
#     assert user_name == 'mapytesting2'
#     assert password == 'mapytesting2@seznam.cz'
#
#
# def test_logout(mobile):
#     main_screen = MainScreen(mobile)
#     main_screen.menu_click()
#
#     menu_screen = MenuScreen(mobile)
#     menu_screen.log_out()
#
#     user_name = mobile.find_element_by_id('cz.seznam.mapy:id/userName').get_attribute('text')
#     assert user_name == 'Log in'


# def test_log_in(browser):
#     my_maps = FirstPage(browser)
#     my_maps.load()
#     my_maps.my_maps()
#
#     login = LoginPage(browser)
#     login.sign_in()


def test_folder_sync(browser, mobile):
    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    login = LoginPage(browser)
    login.sign_in()

    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    my_maps = MyMapsPage(browser)
    my_maps.create_folder()

    # mobile
    # USER_NAME = 'mapytesting2'
    # PASSWORD = 'testingmapy'
    #
    # main_screen = MainScreen(mobile)
    # main_screen.menu_click()
    #
    # menu_screen = MenuScreen(mobile)
    # menu_screen.log_in()
    #
    # login_screen = LogInScreen(mobile)
    # login_screen.user_name(USER_NAME)
    # login_screen.password(PASSWORD)
    # login_screen.sign_in_button()

    # mobile
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.places_and_routes()

    my_maps = MyMapsScreen(mobile)
    my_maps.refresh()

    elem = mobile.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')
    assert elem.get_attribute('text') == 'Changed names'

    # delete folder on web
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/span[2]').click()
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/ul/li[4]').click()

    elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()


def test_poi_changed_name(browser, mobile):
    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    login = LoginPage(browser)
    login.sign_in()

    SEARCH: str = 'Rudolfinum'

    search = FirstPage(browser)
    search.load()
    search.search(SEARCH)

    search = SearchPage(browser)
    # search.close_exact_search()
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.change_name('Poi s vlastním názvem')
    save_page.save()

    # mobile
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.places_and_routes()

    my_maps = MyMapsScreen(mobile)
    my_maps.refresh()

    elem = mobile.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView[1]')
    assert elem.get_attribute('text') == 'Poi s vlastním názvem'

    # delete folder on web

    my_maps = FirstPage(browser)
    my_maps.my_maps()

    # three dots
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[2]/li/div[1]/span[3]').click()
    #delete
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[2]/li/ul/li[6]').click()
    # delete button in dialod window
    elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()



def test_base_poi(browser, mobile):
    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    login = LoginPage(browser)
    login.sign_in()

    SEARCH: str = 'Rudolfinum'

    search = FirstPage(browser)
    search.load()
    search.search(SEARCH)

    search = SearchPage(browser)
    # search.close_exact_search()
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.save()

    # mobile
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.places_and_routes()

    my_maps = MyMapsScreen(mobile)
    my_maps.refresh()

    elem = mobile.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView[1]')
    assert elem.get_attribute('text') == SEARCH

    # delete folder on web

    my_maps = FirstPage(browser)
    my_maps.my_maps()

    # three dots
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[2]/li/div[1]/span[3]').click()
    #delete
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[2]/li/ul/li[6]').click()
    # delete button in dialod window
    elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()