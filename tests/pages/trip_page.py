from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TripPage(object):
    def __init__(self, browser):
        self.browser = browser

    def foot(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By foot']").click()
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='circuit-frame']")))

    def bike(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By bike']").click()
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='circuit-frame']")))

    def change_dist(self):
        elem = self.browser.find_element_by_xpath("//div[@class='circuit-bar-button']")
        ActionChains(self.browser).click_and_hold(elem).move_by_offset(100, 100).release().perform()
        # elem = WebDriverWait(self.browser, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@class='route-weather-form-header']")))


    def save_trip(self):
        elem = self.browser.find_element_by_xpath("//div[@title='Save']").click()