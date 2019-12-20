import locators_mobile
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


class MyMapsScreen(object):
    def __init__(self, mobile):
        self.mobile = mobile

    def refresh(self):
        self.elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/syncButton').click()


    def create_folder(self, name):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/actionButton').click()
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/titleInput').send_keys(name)
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/menu_save').click()

    def order_2_items(self):
        items_name = []
        elem = self.mobile.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')
        items_name.append(elem.get_attribute('text'))
        elem = self.mobile.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[1]')
        items_name.append(elem.get_attribute('text'))
        return items_name

    def reoder_2_items(self):
        elem = self.mobile.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[1]')

        TouchAction(self.mobile).long_press(elem).move_to(x= elem.location['x'], y = elem.location['y'] + 100).release().perform()