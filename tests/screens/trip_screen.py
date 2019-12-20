from appium.webdriver.common.touch_action import TouchAction

class TripScreen(object):
    """docstring for MenuScreen"""

    def __init__(self, mobile):
        self.mobile = mobile

    def foot(self):
        element = self.mobile.find_element_by_xpath('//android.widget.ImageView[@content-desc="Route on foot"]')
        element.click()

    def bike(self):
        element = self.mobile.find_element_by_xpath('//android.widget.ImageView[@content-desc="Route by bike"]')
        element.click()

    def change_distance(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/tripVariantSeekBar')
        #print(el.location)
        #print(el.size)
        TouchAction(self.mobile).tap(x= el.location['x'] + el.size['width'] / 2, y = el.location['y']).perform()

    def save(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/saveButtonLabel')
