from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    def save_trip(self):
        elem = self.browser.find_element_by_xpath("//div[@title='Save']").click()