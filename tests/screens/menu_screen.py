import locators_mobile
from appium.webdriver.common.touch_action import TouchAction


class MenuScreen(object):
    """docstring for MenuScreen"""

    def __init__(self, mobile):
        self.mobile = mobile

    def offline_maps(self):
        elements = self.mobile.find_elements_by_class_name('android.widget.Button')
        for i in elements:
            if i.get_attribute('text') == 'Offline maps':
                i.click()
                break

    def log_in(self):
        self.elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/userName').click()

    def log_out(self):
        self.elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/accountName')
        self.elem.click()
        self.elem = self.mobile.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button')
        self.elem.click()

    def places_and_routes(self):
        elements = self.mobile.find_elements_by_class_name('android.widget.Button')
        for i in elements:
            if i.get_attribute('text') == 'Places and routes':
                i.click()
                break

    def route_planning(self):
        elements = self.mobile.find_elements_by_class_name('android.widget.Button')
        for i in elements:
            if i.get_attribute('text') == 'Route planning':
                i.click()
                break

    def trips(self):
        elements = self.mobile.find_elements_by_class_name('android.widget.Button')
        for i in elements:
            if i.get_attribute('text') == 'Trips nearby':
                i.click()
                break
