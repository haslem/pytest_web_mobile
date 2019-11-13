from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PlanningPage(object):
    def __init__(self, browser):
        self.browser = browser

    def auto(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By car']").click()

    def bike(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By bike']").click()

    def foot(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By foot']").click()

    def boat(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By boat']").click()

    def auto_fast(self):
        elem = self.browser.find_element_by_xpath("//span[text()='Fast']").click()

    def auto_short(self):
        elem = self.browser.find_element_by_xpath("//span[text()='Short']").click()

    def auto_avoid(self):
        elem = self.browser.find_element_by_xpath("//span[text()='Avoid paid tolls']").click()

    def start(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Start']")))
        elem.send_keys('Prague')
        elem.send_keys(u'\ue007')

    def end(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='End']")))
        elem.send_keys('Milan')
        elem.send_keys(u'\ue007')

    def save_route(self):
        elem = self.browser.find_element_by_xpath("//div[@title='Save']").click()
