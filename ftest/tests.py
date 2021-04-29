from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)


	def test_browser_title(self):
		self.browser.get(self.live_server_url)
		self.assertIn('DONATION ENTRY', self.browser.title)

		JdText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('IN-KIND DONATION ENTRY', JdText)

		h_code = self.browser.find_element_by_id('me').text
		self.assertIn('A Bayanihan for the Underprivileged', h_code)

		para = self.browser.find_element_by_tag_name('p').text
		self.assertIn('Type of Donation Support:', para)

		form = self.browser.find_element_by_tag_name('form')

		put1 = self.browser.find_element_by_id('Donor')  
		self.assertEqual(put1.get_attribute('placeholder'),'Name of Donor')
		put1 = self.browser.find_element_by_id('Donor').send_keys("Eden P. Mendoza")
		time.sleep(1)

		put2 = self.browser.find_element_by_id('Email')  
		self.assertEqual(put2.get_attribute('placeholder'),'Email Address')
		put2 = self.browser.find_element_by_id('Email').send_keys("edenpino11@gmail.com")
		time.sleep(1)
		
		put3 = self.browser.find_element_by_id('Donation')  
		self.assertEqual(put3.get_attribute('placeholder'),'Item Donation')
		put3 = self.browser.find_element_by_id('Donation').send_keys("drinks")
		time.sleep(1)

		put4 = self.browser.find_element_by_id('Items')  
		self.assertEqual(put4.get_attribute('placeholder'),'Item Specifics: Volume and Packaging')
		put4 = self.browser.find_element_by_id('Items').send_keys("10L of water")
		time.sleep(1)

		t1 = self.browser.find_element_by_name('tion').click()
		t2 = self.browser.find_element_by_name('tion').click()

		radyo1 = self.browser.find_element_by_id('button1').click()
		time.sleep(1)
		radyo2 = self.browser.find_element_by_id('button2').click()
		time.sleep(1)

		put5 = self.browser.find_element_by_id('Message')  
		self.assertEqual(put5.get_attribute('placeholder'),'Special Instructions')
		put5 = self.browser.find_element_by_id('Message').send_keys("Handle with care")
		time.sleep(1)

		submitbutton = self.browser.find_element_by_name('submit').click()
		time.sleep(2)

		nextpage = self.browser.current_url
		self.assertRegex(nextpage, '/donation/')

		self.browser.quit()	
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)


		put1 = self.browser.find_element_by_id('Donor')  
		self.assertEqual(put1.get_attribute('placeholder'),'Name of Donor')
		put1 = self.browser.find_element_by_id('Donor').send_keys("Ronan Kyle Ranido")
		time.sleep(1)

		put2 = self.browser.find_element_by_id('Email')  
		self.assertEqual(put2.get_attribute('placeholder'),'Email Address')
		put2 = self.browser.find_element_by_id('Email').send_keys("rronankyle@gmail.com")
		time.sleep(1)
		
		put3 = self.browser.find_element_by_id('Donation')  
		self.assertEqual(put3.get_attribute('placeholder'),'Item Donation')
		put3 = self.browser.find_element_by_id('Donation').send_keys("foods")
		time.sleep(1)

		put4 = self.browser.find_element_by_id('Items')  
		self.assertEqual(put4.get_attribute('placeholder'),'Item Specifics: Volume and Packaging')
		put4 = self.browser.find_element_by_id('Items').send_keys("15 sacks of rice")
		time.sleep(1)

		t1 = self.browser.find_element_by_name('tion').click()
		t2 = self.browser.find_element_by_name('tion').click()

		radyo1 = self.browser.find_element_by_id('button1').click()
		time.sleep(1)
		radyo2 = self.browser.find_element_by_id('button2').click()
		time.sleep(1)

		put5 = self.browser.find_element_by_id('Message')  
		self.assertEqual(put5.get_attribute('placeholder'),'Special Instructions')
		put5 = self.browser.find_element_by_id('Message').send_keys("Enjoy it!")
		time.sleep(1)

		submitbutton = self.browser.find_element_by_name('submit').click()
		time.sleep(2)
		
		

		nextpage = self.browser.current_url
		self.assertRegex(nextpage, '/donation/')

		self.browser.quit()

'''if __name__ == '__main__':
	unittest.main()'''

