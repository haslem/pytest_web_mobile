class RouteScreen(object):
    """docstring for MenuScreen"""

    def __init__(self, mobile):
        self.mobile = mobile

    def auto(self):
        el = self.mobile.find_element_by_xpath('//android.widget.ImageView[@content-desc="Route by car"]')
        el.click()

    def foot(self):
        el = self.mobile.find_element_by_xpath('//android.widget.ImageView[@content-desc="Route on foot"]')
        el.click()

    def bike(self):
        el = self.mobile.find_element_by_xpath('//android.widget.ImageView[@content-desc="Route by bike"]')
        el.click()

    def start(self, text):
        elems = self.mobile.find_elements_by_class_name('android.widget.TextView')
        for i in elems:
            if i.get_attribute('text') == 'Start':
                i.click()
                elem = i
                break



        #self.mobile.back()
        elem = self.mobile.find_element_by_id("cz.seznam.mapy:id/input")
        elem.send_keys(text)
        self.mobile.execute_script('mobile: performEditorAction', {'action': 'search'})
        elems = self.mobile.find_elements_by_class_name('android.view.ViewGroup')
        elems[1].click()

    def end(self, text):
        elems = self.mobile.find_elements_by_class_name('android.widget.TextView')
        for i in elems:
            if i.get_attribute('text') == 'End':
                i.click()
                elem = i
                break
        elem = self.mobile.find_element_by_id("cz.seznam.mapy:id/input")
        elem.send_keys(text)
        self.mobile.execute_script('mobile: performEditorAction', {'action': 'search'})
        elems = self.mobile.find_elements_by_class_name('android.view.ViewGroup')
        elems[1].click()


    def options(self):
        elem = self.mobile.find_element_by_id("cz.seznam.mapy:id/routeSettingsButton")
        elem.click()

    def save(self):
        elem = self.mobile.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Save"]/android.widget.ImageView')
        elem.click()


