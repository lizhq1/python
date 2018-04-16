# coding=utf-8
from time import sleep
import datetime, time, random
from selenium.webdriver.common.action_chains import ActionChains
import self

from SRC.common import utils_user

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase( TestCase ):
	def __init__(self, webDriver, paramsList):
			# 请不要修改该方法
		super( EasyCase, self ).__init__( webDriver, paramsList )
	@codeException_dec( '3')
	def runTest(self):

		driver = self.getDriver()
		tool = utils_user
		today = datetime.date.today()
		tomorrow = today + datetime.timedelta( days=1 )

						# 启用周期购业务
		self.OpenMall()
		self.OpenCycle()
		self.save()

								# 新建周期购商品类型
		name=tool.randomStr(6, lowerCaseLetter=True, capitalLetter=True)
		code=random.randint(100,1000)
		self.OpenMallType(name,code)

							   # 设置周期购选择方式
		self.defineCycle("week")
		#self.timelong("input")
		#self.ervermuch("input")
		self.datetimes("week")
		self.MallTypeSave()
	def OpenMall(self):
		driver = self.getDriver()
		driver.find_element_by_xpath( "/html/body/div[1]/div[1]/div/div[1]/ul[8]/li[1]" ).click()
		time.sleep( 3 )
		driver.find_element_by_xpath( "/html/body/div[1]/div[1]/div/div[1]/ul[8]/li[4]/a" ).click()

	def OpenCycle(self):
		driver = self.getDriver()
		driver.find_element_by_xpath( "//form/div[1]/div[2]/div[1]/input[1]" ).click()

	def save(self):
		driver = self.getDriver()
		driver.find_element_by_xpath( "/html/body/div[1]/div[1]/div/div[3]/div/div/div[2]/ul/div/div/button" ).click()
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[8]/li[1]").click()
#打开新增商品类型
	def OpenMallType(self,name,code):
		driver=self.getDriver()
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[3]/li[1]/upmark").click()
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[3]/li[5]/a").click()
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div/a").click()
		time.sleep(2)
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[1]/div/input").send_keys(name)
		time.sleep(3)
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/input").send_keys(code)
		if not driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/input").is_selected():
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[3]/div/input").click()
			time.sleep(3)
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[6]/div/ul/li[5]/a").click()
			js = "var q=document.body.scrollTop=20000"
			driver.execute_script( js )
#配送周期选择
	def defineCycle(self,fag):
		driver=self.getDriver()
		js = "var q=document.body.scrollTop=20000"
		driver.execute_script( js )
		if fag=="day":
			driver.find_element_by_xpath("//table/tbody/tr[1]/td[10]/select").click()
			time.sleep( 3 )
			driver.find_element_by_xpath("//div/table/tbody/tr[1]/td[10]/select/option[1]").click()
		if fag=="week":
			ele=driver.find_element_by_xpath("//table/tbody/tr[1]/td[10]/select")
			time.sleep( 3 )
			ele.find_element_by_xpath("//div/table/tbody/tr[1]/td[10]/select/option[2]").click()
			js = "var q=document.body.scrollTop=10000"
			driver.execute_script( js )
		if fag=="month":
			driver.find_element_by_xpath("//table/tbody/tr[1]/td[10]/select").click()
			time.sleep( 3 )
			driver.find_element_by_xpath("//div/table/tbody/tr[1]/td[10]/select/option[3]").click()

#配送时长选择
	def timelong(self,fag):
		driver=self.getDriver()
		js = "var q=document.body.scrollTop=20000"
		driver.execute_script( js )
		if fag=="input":
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[11]/div/table/tbody/tr[2]/td[8]/select").click()
			time.sleep( 3 )
			driver.find_element_by_xpath("//table/tbody/tr[2]/td[8]/select/option[1]").click()
			time.sleep( 3 )
		if fag=="select":
			driver.find_element_by_xpath("//table/tbody/tr[2]/td[8]/select").click()
			time.sleep( 3 )
			driver.find_element_by_xpath("//table/tbody/tr[2]/td[8]/select/option[2]").click()
			time.sleep( 3 )
			js = "var q=document.body.scrollTop=20000"
			driver.execute_script( js )
#每次配送量选择
	def ervermuch(self,fag):
		driver=self.getDriver()
		if fag=="input":
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[11]/div/table/tbody/tr[3]/td[8]/select").click()
			time.sleep(3)
			driver.find_element_by_xpath("//table/tbody/tr[3]/td[8]/select/option[1]").click()
		if fag=="select":
			driver.find_element_by_xpath( "//tbody/tr[3]/td[8]/select" ).click()
			time.sleep( 3 )
			driver.find_element_by_xpath( "//table/tbody/tr[3]/td[8]/select/option[2]" ).click()
#配送频次的选择
	def datetimes(self,switch):
		driver=self.getDriver()
		if switch=="day":
			js_test = "document.body.scrollTop='20000'"
			driver.execute_script( js_test )
			driver.find_element_by_css_selector("div:nth-child(13) > div > table > tbody > tr:nth-child(5) > td:nth-child(12) > input" ).click()
			for k in range( 1, 5 ):
				driver.find_element_by_css_selector("div:nth-child(13) > div > table > tbody > tr:nth-child(5) > td:nth-child(12) > ul > li:nth-child(" + str(k) + ") > label > input" ).click()
		# 保存
		elif switch=="week":
			js_test = "document.body.scrollTop=2000"
			driver.execute_script( js_test )
			driver.find_element_by_css_selector("div:nth-child(13) > div > table > tbody > tr:nth-child(5) > td:nth-child(12) > input").click()
			for i in range(1,8):
				driver.find_element_by_css_selector("div:nth-child(13) > div > table > tbody > tr:nth-child(5) > td:nth-child(12) > ul > li:nth-child("+str(i)+") > label > input").click()
			time.sleep(3)
			#定位元素
		elif switch=="month":
			js_test = "document.documentElement.scrollTop='20000'"
			driver.execute_script( js_test )
			driver.find_element_by_css_selector("div:nth-child(13) > div > table > tbody > tr:nth-child(5) > td:nth-child(12) > input").click()
			for j in range(1,30):
				driver.find_element_by_css_selector("div:nth-child(13) > div > table > tbody > tr:nth-child(5) > td:nth-child(12) > ul > li:nth-child("+str(j)+") > label > input" ).click()
#保存
	def MallTypeSave(self):
		driver=self.getDriver()
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/div[2]/div[13]/div/button[2]").click()
		time.sleep(3)
		driver.find_element_by_xpath( "/html/body/div[1]/div[1]/div/div[1]/ul[3]/li[1]/upmark" ).click()



