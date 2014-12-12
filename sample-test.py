#ScriptName : Sample-Test.py
#---------------------
from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

import unittest
import time
from random import randint

locator = { 'recentAds'      : ".featured-agencies h2",
			'randomAds'      : "#search-suggestions-box a",
			'querycount'     : ".query-summary",
			'ad_container'   : ".adcontainer",
			'show_more'      : 'button.btn',
			'share_this_ad'  : '.share-this-ad',
			'show_share_link': '[title="Share"] a',
			'share_url'      : '[title="Share"] input',
			'image'          : '.more-holder img'
		   }

baseurl = "https://www.moat.com/"


def ajax_complete(self):
   try:
	   return 0 == driver.execute_script("return jQuery.active")
   except WebDriverException:
	   pass
	
class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.driver.get(baseurl)



	def test_share_this_ad(self):
		links = self.driver.find_elements_by_css_selector(locator['randomAds'])
		link = links[randint(0, len(links)-1)]
		link.click()
		element_to_hover_over = self.driver.find_element_by_css_selector(locator['ad_container'])
		hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
		hover.perform()
		self.driver.execute_script(" $('[title=Share] a').click()")
		share_url = self.driver.execute_script(" return $('[title= \"Share\"] input').val()")
		print share_url
		self.driver.get(share_url)
		self.assertEqual(self.driver.current_url, share_url)





	def test_try_these_are_random(self):
		random_set_1 = []
		ad_list = self.driver.find_elements_by_css_selector(locator['randomAds'])
		for a in ad_list:
			text = a.text
			print text
			random_set_1.append(str(text))
			print random_set_1
		self.driver.refresh()

		random_set_2 = []
		ad_list = self.driver.find_elements_by_css_selector(locator['randomAds'])
		for a in ad_list:
			text = a.text
			print text
			random_set_2.append(str(text))
			print random_set_2
		self.driver.refresh()
			

		random_set_3 = []
		ad_list = self.driver.find_elements_by_css_selector(locator['randomAds'])
		for a in ad_list:
			text = a.text
			print text
			random_set_3.append(str(text))
			print random_set_3

			self.assertNotEqual(random_set_1, random_set_2)
			self.assertNotEqual(random_set_1, random_set_3)
			self.assertNotEqual(random_set_2, random_set_3)

	
	def test_ad_times_less_than_30(self):
			for a in self.driver.find_elements_by_css_selector(locator['recentAds']):
				text = a.text
				print(text)
				minutes = text.split()[0]
				self.assertTrue(int(minutes) <= 30)

	

	def test_add_count(self):
			links = self.driver.find_elements_by_css_selector(locator['randomAds'])
			link = links[randint(0, len(links)-1)]
			print(link.text)
			link.click()
			ad_summary = self.driver.find_element_by_css_selector(locator['querycount']).text.split()[0].replace(",","")
			print ad_summary

			ad_container_count_ini = len(self.driver.find_elements_by_css_selector(locator['ad_container']))
			print ad_container_count_ini
			
			if (ad_summary<=100):
				self.assertEqual(ad_container_count_ini,ad_summary)
			else:
			  	while (self.driver.find_elements_by_css_selector(locator['show_more']).count >= 1):
			  	
			  		self.driver.find_element_by_css_selector(locator['show_more']).click()
			  		try:
			  			img = self.driver.find_elements_by_css_selector(locator['image'])
			  			while(len(img) > 0 and img[0].is_displayed()):
			  				True
			  		except Exception:
			  			print "NoSuchElementException"		
			  			ad_container_count = len(self.driver.find_elements_by_css_selector(locator['ad_container']))
			  			print ad_container_count
			  			self.assertEqual(str(ad_container_count),str(ad_summary))

			
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch)
	unittest.TextTestRunner(verbosity=2).run(suite)
