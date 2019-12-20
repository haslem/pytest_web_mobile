
import locators_mobile
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction



class MainScreen(object):
    """docstring for MainScreen"""
    def __init__(self, mobile):
        super(MainScreen, self).__init__()
        self.mobile = mobile

    def zoom_in(self):
        width = self.mobile.get_window_size()['width']
        height = self.mobile.get_window_size()['height']
        action0 = TouchAction(self.mobile).press(x=width/3, y=height/2 + 20).wait(ms=450).move_to(x=width/3, y=height/2 + 200).release()
        action1 = TouchAction(self.mobile).long_press(x=width/3, y=height/2 - 20).wait(ms=450).move_to(x=width/3, y=height/2 - 200).release()
        action3 = MultiAction(self.mobile)
        action3.add(action0, action1)
        action3.perform()


    def zoom_out(self):
        width = self.mobile.get_window_size()['width']
        height = self.mobile.get_window_size()['height']
        action0 = TouchAction(self.mobile).press(x=width/3, y=height/2 + 200).wait(ms=450).move_to(x=width/3, y=height/2 - 100).release()
        action1 = TouchAction(self.mobile).long_press(x=width/3, y=height/2 - 200).wait(ms=450).move_to(x=width/3, y=height/2 + 100).release()
        action3 = MultiAction(self.mobile)
        action3.add(action0, action1)
        action3.perform()
        print(type(action3))

    def menu_click(self):
        elem = self.mobile.find_element_by_id(locators_mobile.map_screen['menu']).click()
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/content')
        TouchAction(self.mobile).long_press(elem).move_to(x=100, y=100).release().perform()

    def search_click(self):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/searchButton').click()

    def coor(self):
        width = self.mobile.get_window_size()['width']
        height = self.mobile.get_window_size()['height']
        TouchAction(self.mobile).long_press(x=width/3, y=height/2).release().perform()

