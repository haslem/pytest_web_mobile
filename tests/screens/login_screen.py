import locators_mobile



class LogInScreen(object):

    def __init__(self, mobile):
        self.mobile = mobile

    def user_name(self, user_name):
        self.elem = self.mobile.find_element_by_id(locators_mobile.sign_in['email']).send_keys(user_name)

    def password(self, password):
        self.password = password
        self.elem = self.mobile.find_element_by_id(locators_mobile.sign_in['password']).send_keys(password)

    def sign_in_button(self):
        self.elem = self.mobile.find_element_by_xpath(locators_mobile.sign_in['sign_in']).click()


