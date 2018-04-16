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
		self.log_combo_set()

		#新增一
		self.add_button()
		#输入活动名称
		name = tool.randomStr(6, lowerCaseLetter=True, capitalLetter=True)
		self.input_combo_set_name(name)
		self.select_time(tomorrow.strftime('%Y-%m-%d %H:%M:%S'))
		#选择使用渠道
		self.select_channel('online')
		self.select_online_terminal('pc')
		self.select_online_terminal('mbile')
		self.select_online_terminal('weichat')
		self.select_range('allMember')
		#添加商品
		self.add_goods_button()
		self.select_goods()
		self.addgoods_button()
		self.select_type()
		price_one=random.randint(1,10)
		price_two=random.randint(1,10)
		self.input_taocanprice(price_one,price_two)
		self.save_button()

		self.assertEqual(name,self.get_name(),'添加搭配套餐成功')

		self.delete_record()
		self.assertNotEqual(name, self.get_name(), '删除搭配套餐成功')
		'''
		# 新增二
		self.add_button()
		# 输入活动名称
		name1 = tool.randomStr(6, lowerCaseLetter=True, capitalLetter=True)
		self.input_combo_set_name(name1)
		self.select_time(tomorrow.strftime('%Y-%m-%d %H:%M:%S'))
		# 选择使用渠道
		self.select_channel('offline')
		self.select_offline_shop('indicate')
		#选择门店未写
		self.select_range('allCustomer')
		# 选择主商品
		self.add_zgoods_button()
		self.select_zgoods()
		self.addgoods_button()
		# 添加其他商品
		self.add_goods_button()
		self.select_goods()
		self.addgoods_button()
		self.input_zhekou()
		self.select_type()
		self.save_button()

		self.assertEqual(name1, self.get_name(), '添加搭配套餐成功')

		self.delete_record()
		self.assertNotEqual(name1, self.get_name(), '删除搭配套餐成功')


		# 新增二
		self.add_button()
		# 输入活动名称
		name2 = tool.randomStr(6, lowerCaseLetter=True, capitalLetter=True)
		self.input_combo_set_name(name2)
		self.select_time(tomorrow.strftime('%Y-%m-%d %H:%M:%S'))
		# 选择使用渠道
		self.select_channel('all')
		self.select_online_terminal('pc')
		self.select_online_terminal('mbile')
		self.select_online_terminal('weichat')
		self.select_offline_shop('indicate')
		#选择门店未写
		self.select_range('indicateMember')
		# 选择主商品
		self.add_zgoods_button()
		self.select_zgoods()
		self.addgoods_button()
		# 添加其他商品
		self.add_goods_button()
		self.select_goods()
		self.addgoods_button()
		self.input_zhekou()
		self.select_type()
		self.save_button()

		self.assertEqual(name2, self.get_name(), '添加搭配套餐成功')

		self.delete_record()
		self.assertNotEqual(name2, self.get_name(), '删除搭配套餐成功')
		'''
	#进入搭配套餐界面
	def log_combo_set(self):
		driver = self.getDriver()
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[5]/li[1]").click()
		time.sleep(2)
		driver.find_element_by_xpath("//div[1]/ul[5]/li[8]/a").click()
		time.sleep(2)

	#点击新增按钮
	def add_button(self):
		driver = self.getDriver()
		driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/form/div/div/div[2]/a").click()

	#输入活动名称
	def input_combo_set_name(self,name):
		driver = self.getDriver()
		driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/span[2]/input").clear()
		driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/span[2]/input").send_keys(name)
	#选择活动时间
	def select_time(self,startime):
		driver = self.getDriver()
		driver.find_element_by_css_selector('#startDate').clear()
		driver.find_element_by_css_selector('#startDate').send_keys(startime)
		#点击一个月
		driver.find_element_by_css_selector('#quitTimeChange3').click()
	#选择使用渠道
	def select_channel(self,channel):
		driver = self.getDriver()
		if channel=='online':
			if not driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOnlineChannel"]').is_selected():
				driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOnlineChannel"]').click()
			if driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOffLineChannel"]').is_selected():
				driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOffLineChannel"]').click()
		elif channel=='offline':
			if not driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOffLineChannel"]').is_selected():
				driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOffLineChannel"]').click()
			if driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOnlineChannel"]').is_selected():
				driver.find_element_by_css_selector('input[ng-model="combinationsales.applyOnlineChannel"]').click()
		elif channel=='all':
			if not driver.find_element_by_css_selector(
					'input[ng-model="combinationsales.applyOffLineChannel"]').is_selected():
				driver.find_element_by_css_selector(
					'input[ng-model="combinationsales.applyOffLineChannel"]').click()
			if not driver.find_element_by_css_selector(
					'input[ng-model="combinationsales.applyOnlineChannel"]').is_selected():
				driver.find_element_by_css_selector(
					'input[ng-model="combinationsales.applyOnlineChannel"]').click()
	#线上终端
	def select_online_terminal(self,flag):
		driver = self.getDriver()
		if flag=='pc':
			if not driver.find_element_by_css_selector('#terminalType1 > input').is_selected():
				driver.find_element_by_css_selector('#terminalType1 > input').click()
		elif flag=='mbile':
			if not driver.find_element_by_css_selector('#terminalType2 > input').is_selected():
				driver.find_element_by_css_selector('#terminalType2 > input').click()
		elif flag=='weichat':
			if not driver.find_element_by_css_selector('#terminalType4 > input').is_selected():
				driver.find_element_by_css_selector('#terminalType4 > input').click()

	#线下门店
	def select_offline_shop(self,flag):
		driver = self.getDriver()
		if flag=='all':
			if not driver.find_element_by_css_selector('#storeRangeAll').is_selected():
				driver.find_element_by_css_selector('#storeRangeAll').click()
		elif flag=='indicate':
			if not driver.find_element_by_css_selector('#storeRangeIndicate').is_selected():
				driver.find_element_by_css_selector('#storeRangeIndicate').click()
		elif flag=='noIndicate':
			if not driver.find_element_by_css_selector('#storeRangeIndicateNo').is_selected():
				driver.find_element_by_css_selector('#storeRangeIndicateNo').click()

	#买家范围
	def select_range(self,flag):
		driver = self.getDriver()
		if flag == 'allCustomer':
			if not driver.find_element_by_css_selector('#allCustomer').is_selected():
				driver.find_element_by_css_selector('#allCustomer').click()
		elif flag == 'allMember':
			if not driver.find_element_by_css_selector('#allMember').is_selected():
				driver.find_element_by_css_selector('#allMember').click()
		elif flag == 'indicateMember':
			if not driver.find_element_by_css_selector('#indicateMember').is_selected():
				driver.find_element_by_css_selector('#indicateMember').click()
			driver.find_element_by_css_selector('#indicateMemberLevels > span.col-xs-8 > label:nth-child(1)').click()
			driver.find_element_by_css_selector('#indicateMemberLevels > span.col-xs-8 > label:nth-child(2)').click()
			driver.find_element_by_css_selector('#indicateMemberLevels > span.col-xs-8 > label:nth-child(3)').click()
	#点击添加按钮
	def addgoods_button(self):
		driver = self.getDriver()
		driver.find_element_by_css_selector('div.row > div > div:nth-child(1) > div:nth-child(8) > button').click()

	#点击添加商品
	def add_goods_button(self):
		driver = self.getDriver()
		driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[3]/div[1]/div[1]/div[2]").click()

	#选择商品
	def select_goods(self):
		driver = self.getDriver()
		driver.find_element_by_xpath("//table/tbody[1]/tr/td[1]/span/input").click()
		time.sleep(2)
		driver.find_element_by_xpath("//table/tbody[2]/tr/td[1]/span/input").click()
		time.sleep(2)

	#输入套餐价格
	def input_taocanprice(self,price_one,price_two):
		driver = self.getDriver()
		driver.find_element_by_xpath("//table/tbody[1]/tr/th[4]/span/input").send_keys(price_one)
		time.sleep(2)
		driver.find_element_by_xpath("//table/tbody[2]/tr/th[4]/span/input").send_keys(price_two)
		time.sleep(2)
	#选择限购类型
	def select_type(self):
		driver=self.getDriver()
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[3]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/select").click()
		time.sleep(2)
		driver.find_element_by_xpath("//select/option[3]").click()
		time.sleep(2)

	#点击保存
	def save_button(self):
		driver = self.getDriver()
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[3]/div[2]/div[2]/button").click()
		time.sleep(5)

	#删除
	def delete_record(self):
		driver =self.getDriver()
		driver.find_element_by_xpath("//table/tbody/tr[1]/td[6]/span[2]/a").click()
		time.sleep(5)
		driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button[1]").click()
		time.sleep(5)
		driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[5]/li[1]").click()

	#获取第一行秒杀活动名称
	def get_name(self):
		driver = self.getDriver()
		return driver.find_element_by_css_selector('table > tbody > tr > td:nth-child(2) > span','findAssert').text