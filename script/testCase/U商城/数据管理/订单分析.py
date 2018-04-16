# coding=utf-8
from time import sleep
import datetime,time,random
from SRC.common import utils_user

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
	def __init__(self, webDriver,paramsList):
		# 请不要修改该方法
		super(EasyCase, self).__init__(webDriver,paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		tool = utils_user
		today = datetime.date.today()
		tomorrow = today + datetime.timedelta(days=1)
	open()
	def open(self):
		driver=self.getDriver()
		driver.find_element_by.xpath("/html/body/div[1]/div[1]/div/div[1]/ul[12]/li[1]").click()
		time.sleep(3)
		js = "var q=document.documentElement.scrollTop=6000"
		driver.execute_script(js)
		time.sleep(2)
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[12]/li[5]/a").click()
		time.sleep(3)