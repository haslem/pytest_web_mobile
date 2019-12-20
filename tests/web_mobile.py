from appium import webdriver

from screens.main_screen import MainScreen
from screens.menu_screen import MenuScreen
from screens.login_screen import LogInScreen
from screens.my_maps_screen import MyMapsScreen
from screens.folder_screen import FolderScreen

import json
import pytest

from selenium.webdriver import Chrome

from pages.first import FirstPage
from pages.search_page import SearchPage
from pages.my_maps_page import MyMapsPage
from pages.login_page import LoginPage
from pages.save_page import SavePage
from pages.planning_page import PlanningPage
from pages.trip_page import TripPage
from pages.tools_page import ToolsPage
from pages.my_poi_page import MyPoiPage
from pages.measurement_page import MeasurementPage

from selenium.webdriver.common.by import By
#from functions.functions import delete_poi, delete_folder, login, search_element
from functions import functions


def timeout():
    for i in range(100000000):
        pass

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
    functions.login(browser)

    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    my_maps = MyMapsPage(browser)
    my_maps.create_folder('Changed names')

    # #mobile
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
    elem = functions.check_mobile_folder(mobile)
    assert elem.get_attribute('text') == 'Changed names'

    #delete
    functions.delete_folder(mobile)


def test_poi_changed_name(browser, mobile):
    functions.login(browser)

    SEARCH: str = 'Rudolfinum'

    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    # search.close_exact_search()
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.change_name('Poi s vlastním názvem')
    save_page.save()

    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Poi s vlastním názvem'

    # delete folder on web



    functions.delete_poi(mobile)


def test_base_poi(browser, mobile):
    functions.login(browser)

    SEARCH: str = 'Rudolfinum'

    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    # search.close_exact_search()
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.save()

    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == SEARCH

    # delete folder on web
    functions.delete_poi(mobile)



def test_firm_poi(browser, mobile):
    functions.login(browser)

    SEARCH: str = 'Plzeňský restaurant Anděl'

    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    # search.close_exact_search()
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.save()

    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == SEARCH

    # delete folder on web
    functions.delete_poi(mobile)



def test_pubt_poi(browser, mobile):
    functions.login(browser)

    SEARCH: str = 'Zborovská zastávka tramvaje'

    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    try:
        search.search_result_several()
        search.save_exact_match()
    except:
        search.save_exact_match()
    save_page = SavePage(browser)
    save_page.save()

    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Zborovská'

    # delete folder on web
    functions.delete_poi(mobile)


def test_osm_poi(browser, mobile):

    functions.login(browser)

    SEARCH: str = 'London Eye'
    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.save()

    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == SEARCH

    # delete folder on web
    functions.delete_poi(mobile)


def test_country_poi(browser, mobile):

    functions.login(browser)

    SEARCH: str = 'Polsko'
    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.save()

    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Poland'

    # delete folder on web

    functions.delete_poi(mobile)



def test_muni_poi(browser, mobile):

    functions.login(browser)

    SEARCH: str = 'Wurzen'
    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.save()

    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Wurzen'

    # delete folder on web

    functions.delete_poi(mobile)



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




def test_planning1(browser, mobile):

    functions.login(browser)

    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)
    #auto.auto()

    auto.start()
    auto.end()

    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route')
    save_page.save()

    # mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Route'

    # delete folder on web

    functions.delete_poi(mobile)



def test_planning2(browser, mobile):

    functions.login(browser)

    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)
    #auto.auto()

    auto.start()
    auto.end()

    auto.auto_avoid()
    auto.avoid_cr()

    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route avoid cr')
    save_page.save()

    # mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Route avoid cr'

    # delete folder on web

    functions.delete_poi(mobile)


def test_planning3(browser, mobile):
    functions.login(browser)

    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)
    # auto.auto()

    auto.start()
    auto.end()

    auto.auto_avoid()
    auto.avoid_sw()

    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route avoid Switzerland')
    save_page.save()

    # mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Route avoid Switzerland'

    # delete folder on web

    functions.delete_poi(mobile)



def test_planning4(browser, mobile):
    functions.login(browser)

    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)
    auto.auto_short()

    auto.start()
    auto.end()

    auto.auto_avoid()
    auto.avoid_nopay()

    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route avoid pay')
    save_page.save()

    # mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Route avoid pay'

    # delete folder on web

    functions.delete_poi(mobile)


def test_planning5(browser, mobile):
    functions.login(browser)

    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)
    auto.bike()

    auto.start()
    auto.end()

    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route bike')
    save_page.save()

    # mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Route bike'

    # delete folder on web

    functions.delete_poi(mobile)


def test_planning6(browser, mobile):
    functions.login(browser)

    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)
    auto.boat()

    auto.start_boat()
    auto.end_boat()

    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route boat')
    save_page.save()

    # mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Route boat'

    # delete folder on web

    functions.delete_poi(mobile)



def test_planning7(browser, mobile):
    functions.login(browser)

    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)

    auto.foot()
    auto.foot_short()

    auto.start_boat()
    auto.end_boat()



    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route foot short')
    save_page.save()

    # mobile check
    # mobile
    # #elem = functions.check_mobile_item(mobile, 'Route foot short')
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Route foot short'

    # delete folder on web
    timeout()
    functions.delete_poi(mobile)


def test_trip_foot(browser, mobile):

    functions.login(browser)

    trip = FirstPage(browser)
    trip.load()
    trip.trip()

    trip = TripPage(browser)
    #trip.foot()
    trip.save_trip()

    save_page = SavePage(browser)
    save_page.change_name('Foot trip')
    save_page.save()

    #mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Foot trip'

    # delete folder on web

    functions.delete_poi(mobile)


def test_trip_bike(browser, mobile):

    functions.login(browser)

    trip = FirstPage(browser)
    trip.load()
    trip.trip()

    trip = TripPage(browser)
    trip.bike()
    trip.change_dist()
    for i in range(100000000):
        pass
    trip.save_trip()

    save_page = SavePage(browser)
    save_page.change_name('Bike trip')
    save_page.save()

    #mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Bike trip'

    # delete folder on web
    functions.delete_poi(mobile)

def test_my_marks(browser, mobile, num_points):

    functions.login(browser)

    marks = FirstPage(browser)
    marks.load()
    marks.tools()

    marks = ToolsPage(browser)
    marks.my_marks()

    marks = MyPoiPage(browser, num_points)
    marks.add_points()
    marks.rename_last()
    marks.stop_adding()
    marks.save()

    save_page = SavePage(browser)
    save_page.change_name('One point')
    save_page.save()
    #
    # #mobile check
    # # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'One point'

    # delete folder on web
    functions.delete_poi(mobile)



def test_measurement(browser, mobile):

    functions.login(browser)

    measure = FirstPage(browser)
    measure.load()
    measure.tools()

    measure = ToolsPage(browser)
    measure.measurement()

    measure = MeasurementPage(browser)
    measure.add()
    measure.save()

    save_page = SavePage(browser)
    save_page.change_name('Measurement')
    save_page.save()

    #mobile check
    # mobile
    elem = functions.check_mobile_item(mobile)
    assert elem.get_attribute('text') == 'Measurement'

    functions.delete_poi(mobile)


def test_set_home(browser, mobile):

    functions.login(browser)

    home = FirstPage(browser)
    home.my_maps()
    home = MyMapsPage(browser)
    home.set_home()
    for i in range(100000000):
        pass
    home.set_work()


    #mobile check
    # mobile
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.places_and_routes()

    my_maps = MyMapsScreen(mobile)
    my_maps.refresh()

    elem_home = mobile.find_element_by_xpath(
        '//android.widget.FrameLayout[@content-desc="Home: Muzeum"]/android.widget.LinearLayout/android.widget.TextView')
    elem_work = mobile.find_element_by_xpath(
        '//android.widget.FrameLayout[@content-desc="Work: Rudolfinum"]/android.widget.LinearLayout/android.widget.TextView')

    assert elem_home.get_attribute('text') == 'Muzeum' and elem_work.get_attribute('text') == 'Rudolfinum'



def test_create_folder_and_items(browser, mobile):
    functions.login(browser)
    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    my_maps = MyMapsPage(browser)
    my_maps.create_folder('new folder')



    SEARCH: str = 'Rudolfinum'
    functions.search_element(browser, SEARCH)

    search = SearchPage(browser)
    search.save_exact_match()

    save_page = SavePage(browser)
    save_page.select_folder('new folder')
    save_page.save()


    planning = FirstPage(browser)
    planning.load()
    planning.planning()

    auto = PlanningPage(browser)
    # auto.auto()

    auto.start()
    auto.end()

    auto.save_route()

    save_page = SavePage(browser)
    save_page.change_name('Route')
    save_page.select_folder('new folder')
    save_page.save()

    elem = functions.check_mobile_folder(mobile)
    elem = mobile.find_element_by_id('cz.seznam.mapy:id/image').click()
    folder_screen = FolderScreen(mobile)
    print(len(folder_screen.get_titles))

    mobile.back()

    #delete
    functions.delete_folder(mobile)

