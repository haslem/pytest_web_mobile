from selenium.webdriver.common.action_chains import ActionChains

class MeasurementPage(object):
    def __init__(self, browser):
        self.browser = browser

    def add(self):
        elem = self.browser.find_element_by_xpath('//*[@id="map"]')
        for i in range(10):
            if i % 50 == 0:
                # ActionChains(driver).send_keys(u'\ue015').perform()
                ActionChains(self.browser).click_and_hold(elem).move_by_offset(100, 100).release().perform()
            else:
                ActionChains(self.browser).move_by_offset(-10, 0).click().perform()

    def save(self):
        elem = self.browser.find_element_by_xpath("//span[text()='Save']").click()