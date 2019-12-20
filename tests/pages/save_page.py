from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SavePage(object):
    def __init__(self, browser):
        self.browser = browser


    def change_name(self, new_name):
        elem = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/input')

        for i in range(80):
            elem.send_keys(u'\ue003')
        elem.send_keys(new_name)

    def select_folder(self, name):
        elem = self.browser.find_element(By.XPATH, "//h2[text()='My places and routes']").click()
        elem = self.browser.find_element(By.XPATH, f"//span[text()='{name}']").click()

    def save(self):
        try:
            elem = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Save']")))
            elem = self.browser.find_element_by_xpath("//button[text()='Save']").click()

        except:
            elem = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[4]/button[1]')))
            elem = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()

