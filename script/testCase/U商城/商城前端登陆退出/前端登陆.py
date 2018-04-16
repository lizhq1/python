# coding=utf-8
import time

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()

		driver.delete_all_cookies()
		driver.get('http://ceshi.upmalldemo.yonyoucloud.com/login')
		time.sleep( 5 )
		#driver.find_element_by_css_selector('#topbar_member > div:nth-child(2) > a:nth-child(1)').click()
		driver.find_element_by_id('uname').clear()
		driver.find_element_by_id('uname').send_keys("ushangcheng")
		driver.find_element_by_id('password').clear()
		driver.find_element_by_id('password').send_keys("111111")
		driver.find_element_by_id('iptsingup').clear()
		driver.find_element_by_id('iptsingup').send_keys("8dXjt")
		driver.find_element_by_css_selector("button.btn-login.btn.common-btn").click()
		time.sleep(5)
