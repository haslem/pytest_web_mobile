from selenium.webdriver.common.by import By

class SavePage(object):
    def __init__(self, browser):
        self.browser = browser


    def change_name(self, new_name):
        elem = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/input')

        for i in range(80):
            elem.send_keys(u'\ue003')
        elem.send_keys(new_name)

    def save(self):
        elem = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[4]/button[1]').click()


