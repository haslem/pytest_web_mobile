from appium.webdriver.common.touch_action import TouchAction

class PoidetailScreen(object):

    def __init__(self, mobile):
        self.mobile = mobile

    def save(self):
        #elem = self.mobile.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]")
        elems = self.mobile.find_elements_by_class_name('android.widget.TextView')
        for elem in elems:
            if elem.get_attribute('text') == 'Save':
                elem.click()
                break
        #elem = self.mobile.find_element_by_xpath("//*[contains(@name,'btn')]")

    def close(self):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/closeButton').click()
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/closeButton').click()

    def close1(self):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/closeButton').click()

    def scroll_right(self):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/actions')
        x = elem.location['x']
        y = elem.location['y']
        new_x = x + 5
        TouchAction(self.mobile).long_press(elem).move_to(x = new_x, y = y).release().perform()

    def scroll_left(self):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/actions')
        x = elem.location['x']
        y = elem.location['y']
        width = self.mobile.get_window_size()['width']
        new_x = width - 5
        TouchAction(self.mobile).long_press(elem).move_to(x = new_x, y = y).release().perform()

    def trip(self):
        elems = self.mobile.find_elements_by_class_name('android.widget.TextView')
        for elem in elems:
            if elem.get_attribute('text') == 'Trips nearby':
                elem.click()
                print(elem.location)
                break