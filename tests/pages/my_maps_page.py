from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MyMapsPage(object):
    """docstring for SearchPage"""

    EXACT_SEARCH_TITLE_LOC = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/h1')

    def __init__(self, browser):
        super(MyMapsPage, self).__init__()
        self.browser = browser


    def create_folder(self):

        self.elem = self.browser.find_element_by_class_name('make-folder-btn').click()
        # folder name
        self.elem = self.browser.find_element_by_xpath(
                '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/div/div[1]/div[5]/div/input').send_keys("Changed names")
        # save
        elem = self.browser.find_element_by_class_name('save').click()

    def set_home(self):
        elem = self.browser.find_elements_by_xpath("//a[@title='Edit']")
        elem[0].click()
        elem = self.browser.find_element_by_xpath("//input[@type='text']")
        for i in range(80):
            elem.send_keys(u'\ue003')
        elem.send_keys("Muzeum")
        elem.send_keys(u'\ue007')

    def set_work(self):
        elem = self.browser.find_elements_by_xpath("//a[@title='Edit']")
        elem[1].click()
        elem = self.browser.find_element_by_xpath("//input[@type='text']")
        for i in range(80):
            elem.send_keys(u'\ue003')
        elem.send_keys("Rudolfinum")
        elem.send_keys(u'\ue007')
