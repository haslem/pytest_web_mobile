import locators


class LoginPage(object):
    """docstring for SearchPage"""


    def __init__(self, browser):
        super(LoginPage, self).__init__()
        self.browser = browser
        self.login = 'mapytesting2'
        self.password = 'testingmapy'

    def sign_in(self):
        # signIn
        self.elem = self.browser.find_element_by_xpath(locators.register['signIn'])
        self.elem.click()
        self.handle = self.browser.window_handles

        # print(handle[1])
        self.browser.switch_to.window(self.handle[1])
        self.elem = self.browser.find_element_by_xpath(locators.register['mail']).send_keys(self.login)
        self.elem = self.browser.find_element_by_xpath(locators.register['pass']).send_keys(self.password)
        self.elem = self.browser.find_element_by_xpath(locators.register['enter']).click()
        # timeOut()
        self.handle = self.browser.window_handles
        self.browser.switch_to.window(self.handle[0])
