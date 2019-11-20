from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstPage(object):

    URL = 'https://en.mapy.cz/zakladni?x=14.3999996&y=50.0499992&z=17'
    SEARCH_INPUT_LOC = (By.ID, 'input-search')
    CHANGE_MAP_LOC = (By.CSS_SELECTOR, '.icon.mapset')

    """docstring for FirstPage"""
    def __init__(self, browser):
        super(FirstPage, self).__init__()
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)


    def search(self, search):
        search_input = self.browser.find_element(*self.SEARCH_INPUT_LOC)
        search_input.send_keys(search)
        search_input.send_keys(u'\ue007')

    def change_map(self):
        self.elem = self.browser.find_element(By.CSS_SELECTOR, '.icon.mapset').click()
        self.maps =  self.browser.find_elements_by_tag_name('li')
        return self.maps


        # def base(self):
        # 	self.maps[-16].click()

        # def historic(self):
        # 	self.maps[-4].click()

    def change_map_historic(self):
        self.change_map()[-4].click()


    def my_maps(self):
        #self.elem = self.browser.find_element(By.CSS_SELECTOR, ".icon.mymap").click()
        self.elem = self.browser.find_element(By.XPATH, "//span[text()='My maps']").click()

    def planning(self):
        elem = self.browser.find_element(By.XPATH, "//button[@class='icon route']").click()

    def tools(self):
        self.elem = self.browser.find_element(By.CSS_SELECTOR, ".icon.tools").click()


    def coor(self):
        elem = self.browser.find_element_by_id('map')
        elem.click()

        ActionChains(self.browser).move_by_offset(100, 100).context_click().perform()
        elem = self.browser.find_element_by_partial_link_text('What')
        elem.click()

    def trip(self):
        elem = self.browser.find_element_by_id('map')
        elem.click()

        ActionChains(self.browser).move_by_offset(100, 100).context_click().perform()
        elem = self.browser.find_element_by_partial_link_text('Trip')
        elem.click()

