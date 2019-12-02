from appium import webdriver

from screens.main_screen import MainScreen
from screens.menu_screen import MenuScreen
from screens.login_screen import LogInScreen
from screens.my_maps_screen import MyMapsScreen
from screens.search_screen import SearchScreen
from screens.poidetail_screen import PoidetailScreen
from screens.save_screen import SaveScreen

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

from functions import functions
from functions import functions_mobile


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
    my_maps.create_folder('Changed names')


    elem = functions.check_web_item(browser)
    assert elem.text == 'Changed names'


    # #delete folder
    functions.delete_folder(mobile)



def test_mobile_poi_changed_name(browser, mobile):

    SEARCH: str = 'Gherkin'

    search_screen = MainScreen(mobile)
    search_screen.search_click()
    search = SearchScreen(mobile)
    search.search(SEARCH)

    poidetail = PoidetailScreen(mobile)
    #poidetail.scroll()
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.rename("New name")
    save_page.save()




    poidetail = PoidetailScreen(mobile)
    poidetail.close()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()


    elem = functions.check_web_item(browser)
    assert elem.text == 'New name'

    # #delete poi
    functions.delete_poi(mobile)



def test_mobile_base_poi(browser, mobile):
    SEARCH: str = 'Rudolfinum'

    search_screen = MainScreen(mobile)
    search_screen.search_click()
    search = SearchScreen(mobile)
    search.search(SEARCH)

    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == SEARCH



def test_mobile_firm_poi(browser, mobile):

    SEARCH: str = 'Plzeňský restaurant Anděl'

    search_screen = MainScreen(mobile)
    search_screen.search_click()
    search = SearchScreen(mobile)
    search.search(SEARCH)

    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == SEARCH



def test_mobile_pubt_poi(browser, mobile):

    SEARCH: str = 'Zborovská zastávka tramvaje'

    search_screen = MainScreen(mobile)
    search_screen.search_click()
    search = SearchScreen(mobile)
    search.search(SEARCH)

    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == SEARCH


def test_mobile_osm_poi(browser, mobile):

    SEARCH: str = 'London Eye'
    search_screen = MainScreen(mobile)
    search_screen.search_click()
    search = SearchScreen(mobile)
    search.search(SEARCH)

    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == SEARCH


def test_mobile_country_poi(browser, mobile):

    SEARCH: str = 'Polsko'
    search_screen = MainScreen(mobile)
    search_screen.search_click()
    search = SearchScreen(mobile)
    search.search(SEARCH)

    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == SEARCH



def test_mobile_muni_poi(browser, mobile):

    SEARCH: str = 'Wurzen'
    search_screen = MainScreen(mobile)
    search_screen.search_click()
    search = SearchScreen(mobile)
    search.search(SEARCH)

    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == SEARCH



def test_coor_changed_name(browser, mobile):

    functions.login(browser)

    coor = FirstPage(browser)
    coor.load()
    coor.coor()

    poi = SearchPage(browser)
    poi.save_exact_match()

    save_page = SavePage(browser)
    save_page.save()

    #mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Position on the map'

    # delete folder on web

    functions.delete_poi(mobile)


def test_coor_changed_name_rename(browser, mobile):

    functions.login(browser)

    coor = FirstPage(browser)
    coor.load()
    coor.coor()

    poi = SearchPage(browser)
    poi.save_exact_match()

    save_page = SavePage(browser)
    save_page.change_name('Coor s vlastním názvem')
    save_page.save()

    #mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Coor s vlastním názvem'

    # delete folder on web

    functions.delete_poi(mobile)