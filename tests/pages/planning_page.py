from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def timeout():
    for _ in range(10000000):
        pass


class PlanningPage(object):
    def __init__(self, browser):
        self.browser = browser

    def auto(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By car']").click()

    def bike(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By bike']").click()

    def foot(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By foot']").click()

    def foot_short(self):
        elem = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/label[1]/input").click()

    def foot_tourist(self):
        elem = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/label[2]/input").click()

    def boat(self):
        elem = self.browser.find_element_by_xpath("//input[@aria-label='By boat']").click()

    def auto_fast(self):
        elem = self.browser.find_element_by_xpath("//span[text()='Fast']").click()

    def auto_short(self):
        elem = self.browser.find_element_by_xpath("//span[text()='Short']").click()

    def auto_avoid(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='route-traffic-form-header']")))
        elem = self.browser.find_element_by_xpath("//span[text()='Avoid paid tolls']").click()


    def avoid_cr(self):
        elem = self.browser.find_element_by_xpath("//p[text()='Czechia']").click()

    def avoid_sw(self):
        elem = self.browser.find_element_by_xpath("//p[text()='Switzerland']").click()

    def avoid_nopay(self):
        elem = self.browser.find_element_by_xpath("//p[text()='Avoid tolls everywhere']").click()

    def start(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Start']")))
        elem.send_keys('Prague')
        elem.send_keys(u'\ue007')

    def end(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='End']")))
        elem.send_keys('Genoa')
        elem.send_keys(u'\ue007')


    def start_boat(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Start']")))
        elem.send_keys('Most Legii')
        elem.send_keys(u'\ue007')
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Trips nearby']")))


    def end_boat(self):
        elem = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='End']")))
        elem.send_keys('Jiraskuv most')
        elem.send_keys(u'\ue007')

    def save_route(self):
        elem = self.browser.find_element_by_xpath("//div[@title='Save']").click()

