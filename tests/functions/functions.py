from pages.first import FirstPage
from pages.search_page import SearchPage
from pages.my_maps_page import MyMapsPage
from pages.login_page import LoginPage
from pages.save_page import SavePage


from screens.main_screen import MainScreen
from screens.menu_screen import MenuScreen
from screens.login_screen import LogInScreen
from screens.my_maps_screen import MyMapsScreen


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

def delete_poi(browser):

#     #delete from web
#     for i in range(100000000):
#         pass
#     my_maps = FirstPage(browser)
#     my_maps.my_maps()
#
#
#     #pass
#     elem = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[2]/li/div[1]/span[3]')))
#
# # three dots
#     elem = browser.find_element_by_xpath(
#         '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[2]/li/div[1]/span[3]').click()
#     #delete
#     elem = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//h3[text()='Delete']")))
#     elem = browser.find_element_by_xpath(
#         "//h3[text()='Delete']").click()
#     # delete button in dialod window
#     elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()



    #delete from mobile
    elem = browser.find_element_by_id('cz.seznam.mapy:id/moreButton').click()
    elem = browser.find_element_by_xpath("//android.widget.TextView[@text='Delete']").click()
    try:
        elem = browser.find_element_by_id('android:id/button1').click()

    except:
        elem = browser.find_element_by_id("cz.seznam.mapy:id/menu_mymaps_delete").click()
        elem = browser.find_element_by_id('android:id/button1').click()




def delete_folder(browser):
    # # delete folder on web
    # elem = browser.find_element_by_xpath(
    #     '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/span[2]').click()
    # elem = browser.find_element_by_xpath(
    #     '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/ul/li[4]').click()
    #
    # elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()


    #delete from mobile
    elem = browser.find_element_by_id('cz.seznam.mapy:id/moreButton').click()
    elem = browser.find_element_by_xpath("//android.widget.TextView[@text='Delete']").click()
    try:
        elem = browser.find_element_by_id('android:id/button1').click()

    except:
        elem = browser.find_element_by_id("cz.seznam.mapy:id/menu_mymaps_delete").click()
        elem = browser.find_element_by_id('android:id/button1').click()


def login(browser):
    my_maps = FirstPage(browser)
    my_maps.load()
    my_maps.my_maps()

    login = LoginPage(browser)
    login.sign_in()


def search_element(browser, SEARCH):
    search = FirstPage(browser)
    search.load()
    search.search(SEARCH)


def check_mobile_folder(mobile):
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.places_and_routes()

    my_maps = MyMapsScreen(mobile)
    my_maps.refresh()

    elem = mobile.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')

    # elem = mobile.find_element_by_xpath(
    #     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')
    return  elem


def check_web_folder(browser):
    # web check
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
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/h2")))
    return  elem


def check_mobile_item(mobile):
    #pass
    main_screen = MainScreen(mobile)
    main_screen.menu_click()

    menu_screen = MenuScreen(mobile)
    menu_screen.places_and_routes()

    my_maps = MyMapsScreen(mobile)
    my_maps.refresh()


    #elem = mobile.find_element_by_xpath(f'//*[@text = {element_title}]')
    elem = mobile.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView[1]')
    elem.get_attribute('text')
    return elem


def check_web_item(browser):
    # web check
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
        EC.presence_of_element_located(
            (By.XPATH, "//h2[@class='title overflow-ellipsis']")))
    elem = browser.find_element_by_xpath("//h2[@class='title overflow-ellipsis']")
    return elem


def return_web_items(browser):
    # web check
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
        EC.presence_of_element_located(
            (By.XPATH, "//h2[@class='title overflow-ellipsis']")))
    elems = browser.find_elements_by_xpath("//h2[@class='title overflow-ellipsis']")
    return elems