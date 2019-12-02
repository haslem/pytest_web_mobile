
class SaveScreen(object):

    def __init__(self, mobile):
        self.mobile = mobile

    def rename(self, new_name):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/titleInput')

        # for i in range(50):
        #     elem.send_keys(u'\ue003')

        # elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/menu_save').click()
        #elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/titleInput')
        elem.send_keys(u'\ue003')
        elem.send_keys(new_name)



    def save(self):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/menu_save').click()
