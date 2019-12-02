
class SearchScreen(object):

    def __init__(self, mobile):
        self.mobile = mobile


    def search(self, search):
        elem = self.mobile.find_element_by_id('cz.seznam.mapy:id/input').send_keys(search)
        self.mobile.execute_script('mobile: performEditorAction', {'action': 'search'})
        #elem.send_keys(u'\ue007')