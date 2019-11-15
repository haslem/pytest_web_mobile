from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyPoiPage(object):
    def __init__(self, browser, num_points):
        self.browser = browser
        self.num_points = num_points

    def add_points(self):
        # select map
        elem = self.browser.find_element_by_xpath('//*[@id="map"]')

        for i in range(self.num_points):
            ActionChains(self.browser).move_by_offset(-10, 0).click().perform()

    def rename_last(self):
        elem = self.browser.find_elements(By.CLASS_NAME, 'title-input')
        elem[-1].send_keys('Last')

    def stop_adding(self):
        try:
            elem = self.browser.find_element_by_xpath("//button[@class='save-btn']").click()
        except:
            xpath = '/html/body/div/div[2]/div[2]/div[1]/div/div/div[2]/ul/li[' +f'{self.num_points}' + ']/div[2]/div[2]/button[1]'
            elem = self.browser.find_element_by_xpath(xpath).click()


    def save(self):

        elem = self.browser.find_element_by_xpath("//span[text()='Save']").click()
