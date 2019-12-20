from appium import webdriver


from screens.main_screen import MainScreen
from screens.menu_screen import MenuScreen
from screens.login_screen import LogInScreen
from screens.my_maps_screen import MyMapsScreen
from screens.search_screen import SearchScreen
from screens.poidetail_screen import PoidetailScreen
from screens.save_screen import SaveScreen
from screens.route_screen import RouteScreen
from screens.options_screen import OptionsScreen
from screens.trip_screen import TripScreen

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
    poidetail.scroll_right()
    poidetail.scroll_left()
    #poidetail.trip()
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

    # #delete poi
    functions.delete_poi(mobile)



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
    # #delete poi
    functions.delete_poi(mobile)


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
    assert elem.text == 'Zborovská'
    # #delete poi
    functions.delete_poi(mobile)

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
    # #delete poi
    functions.delete_poi(mobile)

def test_mobile_country_poi(browser, mobile):

    SEARCH: str = 'Poland'
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
    # #delete poi
    functions.delete_poi(mobile)


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

    # #delete poi
    functions.delete_poi(mobile)

def test_mobile_coor_changed_name(browser, mobile):

    search_screen = MainScreen(mobile)
    search_screen.coor()
    #search_screen.zoom_in()
    #earch_screen.zoom_out()


    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    #save_page.rename("New name")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()



    elem = functions.check_web_item(browser)
    assert elem.text == "Position on the map"

    # #delete poi
    functions.delete_poi(mobile)



def test_mobile_coor_changed_name_rename(browser, mobile):
    search_screen = MainScreen(mobile)
    search_screen.coor()
    #search_screen.zoom_in()
    #earch_screen.zoom_out()


    poidetail = PoidetailScreen(mobile)
    poidetail.save()

    save_page = SaveScreen(mobile)
    save_page.rename("New name coor")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()



    elem = functions.check_web_item(browser)
    assert elem.text == "New name coor"

    # #delete poi
    functions.delete_poi(mobile)


def test_mobile_planning1(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.route_planning()
    planning = RouteScreen(mobile)
    planning.start("Prague")
    planning.end("Genoa")
    for i in range(100000000):
        pass
    planning.save()

    save_page = SaveScreen(mobile)
    #save_page.rename("New name")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()



    elem = functions.check_web_item(browser)
    assert elem.text == "Route from Prague to Genoa"

    # #delete poi
    functions.delete_poi(mobile)




def test_mobile_planning2(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.route_planning()
    planning = RouteScreen(mobile)
    planning.start("Prague")
    planning.end("Genoa")
    for i in range(200000000):
        pass
    planning.options()

    options = OptionsScreen(mobile)
    options.avoid_cr()
    mobile.back()
    for i in range(100000000):
        pass

    planning = RouteScreen(mobile)

    planning.save()

    save_page = SaveScreen(mobile)
    save_page.rename("Route avoid cr")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == "Route avoid cr"

    # #delete poi
    functions.delete_poi(mobile)


def test_mobile_planning3(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.route_planning()
    planning = RouteScreen(mobile)
    planning.start("Prague")
    planning.end("Genoa")
    for i in range(200000000):
        pass
    planning.options()

    options = OptionsScreen(mobile)
    options.avoid_sw()
    mobile.back()
    for i in range(100000000):
        pass

    planning = RouteScreen(mobile)

    planning.save()

    save_page = SaveScreen(mobile)
    save_page.rename("Route avoid switzerland")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == "Route avoid switzerland"

    # #delete poi
    functions.delete_poi(mobile)


def test_mobile_planning4(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.route_planning()
    planning = RouteScreen(mobile)
    planning.start("Prague")
    planning.end("Genoa")
    for i in range(200000000):
        pass
    planning.options()

    options = OptionsScreen(mobile)
    options.auto_avoid()
    options.auto_short()
    mobile.back()
    for i in range(100000000):
        pass

    planning = RouteScreen(mobile)

    planning.save()

    save_page = SaveScreen(mobile)
    save_page.rename("Route avoid pay short")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == "Route avoid pay short"

    # #delete poi
    functions.delete_poi(mobile)


def test_mobile_planning5(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.route_planning()
    planning = RouteScreen(mobile)
    planning.bike()
    planning.start("Prague")
    planning.end("Genoa")

    for i in range(100000000):
        pass

    planning = RouteScreen(mobile)

    planning.save()

    save_page = SaveScreen(mobile)
    save_page.rename("Bike route")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == "Bike route"

    # #delete poi
    functions.delete_poi(mobile)


def test_mobile_planning6(browser, mobile):
    #for boat
    pass


def test_mobile_planning7(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.route_planning()
    planning = RouteScreen(mobile)
    planning.foot()
    planning.options()
    options = OptionsScreen(mobile)
    options.foot_short()
    mobile.back()
    planning.start("Prague")
    planning.end("Genoa")

    for i in range(100000000):
        pass

    planning = RouteScreen(mobile)

    planning.save()

    save_page = SaveScreen(mobile)
    save_page.rename("Foot route")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == "Foot route"

    # #delete poi
    functions.delete_poi(mobile)



def test_mobile_trip_foot(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.trips()

    for i in range(100000000):
        pass

    trip = TripScreen(mobile)
    # trip.change_distance()
    # for i in range(100000000):
    #     pass

    trip.save()
    save_page = SaveScreen(mobile)
    name = save_page.get_name()
    #save_page.rename("Foot trip")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == name

    # #delete poi
    functions.delete_poi(mobile)


def test_mobile_trip_bike_distance(browser, mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.trips()

    for i in range(100000000):
        pass

    trip = TripScreen(mobile)
    trip.bike()
    for i in range(100000000):
        pass
    trip.change_distance()
    for i in range(100000000):
        pass

    trip.save()
    save_page = SaveScreen(mobile)
    name = save_page.get_name()
    #save_page.rename("Bike change distance")
    save_page.save()

    poidetail = PoidetailScreen(mobile)
    poidetail.close1()
    poidetail.close1()

    main_screen = MainScreen(mobile)
    main_screen.menu_click()
    menu = MenuScreen(mobile)
    menu.places_and_routes()

    elem = functions.check_web_item(browser)
    assert elem.text == name

    # #delete poi
    functions.delete_poi(mobile)


def test_mobile_reorder(browser, mobile):

    countries = ['Poland', 'Sweden']
    for SEARCH in countries:
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

    my_maps = MyMapsScreen(mobile)
    order = my_maps.order_2_items()


    elems = functions.return_web_items(browser)
    web_order = []
    for i in elems:
        web_order.append(i.text)

    print(order)
    print(web_order)

    assert order == web_order

    my_maps.reoder_2_items()


    # # #delete poi
    # functions.delete_poi(mobile)



















