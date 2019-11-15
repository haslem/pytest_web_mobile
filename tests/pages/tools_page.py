class ToolsPage(object):
    def __init__(self, browser):
        self.browser = browser


    def my_marks(self):
        elem = self.browser.find_element_by_xpath("//div[@class='shitem si-usermarks']").click()

    def measurement(self):
        elem = self.browser.find_element_by_xpath("//div[@class='shitem si-distanceMeter']").click()