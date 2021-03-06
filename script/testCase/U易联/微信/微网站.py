# coding=utf-8
import time

from selenium.webdriver import ActionChains

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

		driver.find_element_by_css_selector("#page_module > li:nth-child(4) > a").click()
		time.sleep(5)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div:nth-child(1)").click()
		time.sleep(3)
		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(4) > p").click()
		time.sleep(3)

		# 编辑
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(1)").click()
		time.sleep(1)
		s1=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cWebSiteName").clear()
		driver.find_element_by_id("cWebSiteName").send_keys(s1)
		time.sleep(1)

		driver.find_element_by_id("topSaveBtn").click()
		time.sleep(2)

		driver.find_element_by_css_selector("#m-zone > div.mode > ul > li:nth-child(1) > a").click()
		time.sleep(2)
		driver.find_element_by_id("menues_cMenuName").clear()
		driver.find_element_by_id("menues_cMenuName").send_keys("fdd")
		time.sleep(1)
		driver.find_element_by_css_selector(
			"#box-content1 > div.form-group.radio-group > span > label:nth-child(2) > input").click()
		time.sleep(1)
		driver.find_element_by_id("menues_cLinkUrl").send_keys("123123")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()

		driver.find_element_by_xpath('//a[@href="/Page/WAP/WebsiteList"]').click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s1, '新增失败')

		# 删除
		driver.find_element_by_css_selector(
			"#datagrid > tbody > tr:nth-child(1) > td.center.text-nowrap > a:nth-child(2)").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 新增
		driver.find_element_by_id("exportAction").click()
		time.sleep(2)

		driver.find_element_by_css_selector("#hometemplate > div > img").click()
		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(3)
		s2=tool.randomStr(4,False,True,True)
		driver.find_element_by_id("cWebSiteName").clear()
		driver.find_element_by_id("cWebSiteName").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_id("topSaveBtn").click()
		time.sleep(2)

		# 模板编写
		driver.find_element_by_css_selector("#m-zone > div.mode > ul > li:nth-child(1) > a").click()

		driver.find_element_by_id("menues_cMenuName").clear()
		driver.find_element_by_id("menues_cMenuName").send_keys("fdd")
		time.sleep(1)

		driver.find_element_by_css_selector(
			"#box-content1 > div.form-group.radio-group > span > label:nth-child(1) > input").click()
		time.sleep(2)

		driver.find_element_by_css_selector("#menues_btnCate").click()
		time.sleep(2)

		driver.find_element_by_css_selector("#catetemplate > ul:nth-child(2) > li > a").click()

		driver.find_element_by_id("btnDialogBySHFConfirm").click()
		time.sleep(1)

		# 二级菜单编写
		# m-zone > div.mode > ul > li > a > div
		driver.find_element_by_css_selector("#m-zone > div.mode > ul > li > a > div").click()
		time.sleep(1)

		driver.find_element_by_id("menues_cMenuName").clear()
		driver.find_element_by_id("menues_cMenuName").send_keys("swq")
		time.sleep(2)

		driver.find_element_by_id("menues_cSummary").send_keys("123")
		time.sleep(1)

		driver.find_element_by_css_selector(
			"#box-content1 > div.form-group.radio-group > span > label:nth-child(1) > input").click()
		driver.find_element_by_id("menues_cLinkUrl").send_keys("123123")
		time.sleep(1)

		driver.find_element_by_id("saveAction").click()
		time.sleep(2)

		driver.find_element_by_css_selector("#page_menu > li:nth-child(2) > div.typ > a:nth-child(4) > p").click()
		time.sleep(3)
		# 新增/复制/编辑验证
		new = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(new, s2, '新增失败')

		# 查询

		driver.find_element_by_id("query_cWebSiteName").send_keys(s2)
		time.sleep(1)

		driver.find_element_by_id("query_search").click()
		time.sleep(5)

		# 查询验证
		search = driver.find_element_by_css_selector("#datagrid > tbody > tr:nth-child(1) > td:nth-child(1)","findAssert").text
		self.assertEqual(search, s2, "查询成功")
