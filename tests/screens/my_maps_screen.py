import locators_mobile
from selenium.webdriver.common.by import By


class MyMapsScreen(object):
    def __init__(self, mobile):
        self.mobile = mobile

    def refresh(self):
        self.elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/syncButton').click()


    def create_folder(self, name):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/actionButton').click()
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/titleInput').send_keys(name)
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/menu_save').click()