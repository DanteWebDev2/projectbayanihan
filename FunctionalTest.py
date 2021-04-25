from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

"""import unittest
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_browser_test(self):
		self.browser.get.browser('http://localhost:8000')
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		#self.assertIn('BALANCE Group', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('In-Kind Donation', headerText)
		inputbox = self.browser.find_element_by_id('idNewEntry').send_keys("4000-xxx")
		
		inputbox = self.browser.find_element_by_id('newEntry2')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'dd/mm/yr')
		inputbox.send_keys('July 24, 1999')
		inputbox.send_keys(Keys.ENTER)



if __name__ == '__main__':
	unittest.main(warnings='ignore')"""