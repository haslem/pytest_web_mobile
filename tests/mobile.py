import json
import pytest
from appium import webdriver

from screens.main_screen import MainScreen
from screens.menu_screen import MenuScreen
from screens.login_screen import LogInScreen


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


def test_menu_button(mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()


def test_offlinemaps_button(mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.offline_maps()


def test_login(mobile):
    USER_NAME = 'mapytesting2'
    PASSWORD = 'testingmapy'

    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.log_in()

    login_screen = LogInScreen(mobile)
    login_screen.user_name(USER_NAME)
    login_screen.password(PASSWORD)
    login_screen.sign_in_button()

    user_name = mobile.find_element_by_id('cz.seznam.mapy:id/userName').get_attribute('text')
    password = mobile.find_element_by_id('cz.seznam.mapy:id/accountName').get_attribute('text')

    assert user_name == 'mapytesting2'
    assert password == 'mapytesting2@seznam.cz'


def test_logout(mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.log_out()

    user_name = mobile.find_element_by_id('cz.seznam.mapy:id/userName').get_attribute('text')
    assert user_name == 'Log in'
