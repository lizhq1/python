# coding=utf-8
import time

from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils


class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool = utils_user

		driver.find_element_by_css_selector("#page_module > li:nth-child(3) > a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(1) > p").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(1) > div.typ > a:nth-child(8) > p").click()
		time.sleep(3)

		# start time
		driver.find_element_by_id("start").send_keys("2016-06-07")

		# end time
		driver.find_element_by_id("end").send_keys("2016-07-07")

		ggh = driver.find_element_by_css_selector("#selArea > table > tbody > tr > td:nth-child(6) > span > span")
		ggh.find_element_by_css_selector(
			"#selArea > table > tbody > tr > td:nth-child(6) > span > span > span.k-input").click()
		driver.find_element_by_id("sel_Button").click()