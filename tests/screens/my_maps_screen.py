import locators_mobile
from selenium.webdriver.common.by import By


class MyMapsScreen(object):
    def __init__(self, mobile):
        self.mobile = mobile

    def refresh(self):
        self.elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/syncButton').click()