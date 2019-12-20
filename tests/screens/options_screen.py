class OptionsScreen(object):
    """docstring for MenuScreen"""

    def __init__(self, mobile):
        self.mobile = mobile


    def auto_avoid(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/avoidAllSwitch')
        el.click()


    def avoid_cr(self):
        el = self.mobile.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Switch')
        el.click()


    def avoid_sw(self):
        el = self.mobile.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[4]/android.widget.Switch')
        el.click()




    def auto_fast(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/fastButton')
        el.click()

    def auto_short(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/shortButton')
        el.click()



    def foot_tourist(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/leftButton')
        el.click()


    def foot_short(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/rightButton')
        el.click()


    def bike_mountain(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/leftButton')
        el.click()


    def bike_road(self):
        el = self.mobile.find_element_by_id('cz.seznam.mapy:id/rightButton')
        el.click()