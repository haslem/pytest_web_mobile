
import locators_mobile
from appium.webdriver.common.touch_action import TouchAction


class MainScreen(object):
	"""docstring for MainScreen"""
	def __init__(self, mobile):
		super(MainScreen, self).__init__()
		self.mobile = mobile

		
	def menu_click(self):
		elem = self.mobile.find_element_by_id(locators_mobile.map_screen['menu']).click()
		elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/content')
		TouchAction(self.mobile).long_press(elem).move_to(x=100, y=100).release().perform()	
