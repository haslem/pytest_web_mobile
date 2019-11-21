from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SearchPage(object):
	"""docstring for SearchPage"""

	EXACT_SEARCH_TITLE_LOC = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]/h1')

	def __init__(self, browser):
		super(SearchPage, self).__init__()
		self.browser = browser


	def search_result(self):
		WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((self.EXACT_SEARCH_TITLE_LOC[0], self.EXACT_SEARCH_TITLE_LOC[1])))

		#print(*self.EXACT_SEARCH_TITLE_LOC)
		elem = self.browser.find_element(*self.EXACT_SEARCH_TITLE_LOC)	
		return elem.text

	def search_result_several(self):
		WebDriverWait(self.browser, 10).until(
			EC.presence_of_element_located((By.ID, 'search-results')))

		# print(*self.EXACT_SEARCH_TITLE_LOC)
		elem = self.browser.find_element(By.XPATH, "//a[@class='li-inner']").click()


	def save_exact_match(self):
		# save poi, star button
		elem = WebDriverWait(self.browser, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='icon-action']")))
		elem = self.browser.find_elements(By.CSS_SELECTOR, "div[class='icon-action']")
		elem[1].click()

	def close_exact_search(self):
		elem = self.browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]/div[2]/button').click()