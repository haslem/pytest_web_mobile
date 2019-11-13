from pages.first import FirstPage
from pages.search_page import SearchPage
from pages.my_maps_page import MyMapsPage
from pages.login_page import LoginPage
from pages.save_page import SavePage


def delete_poi(browser):

# three dots
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[2]/li/div[1]/span[3]').click()
    #delete
    elem = browser.find_element_by_xpath(
        "//h3[text()='Delete']").click()
    # delete button in dialod window
    elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()



def delete_folder(browser):
    # delete folder on web
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/span[2]').click()
    elem = browser.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/ul[1]/li/div/div[2]/ul/li[4]').click()

    elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/button[1]').click()


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

