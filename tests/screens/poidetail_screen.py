from appium.webdriver.common.touch_action import TouchAction

class PoidetailScreen(object):

    def __init__(self, mobile):
        self.mobile = mobile

    def save(self):
        elem = self.mobile.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]")
        elem.click()
        #elem = self.mobile.find_element_by_xpath("//*[contains(@name,'btn')]")

    def close(self):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/closeButton').click()
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/closeButton').click()

    def scroll(self):
        elem = self.mobile.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]")
        TouchAction(self.mobile).long_press(elem).move_to(x=100, y=0).release().perform()