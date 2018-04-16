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

    #打开固定套餐
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[5]/li[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[1]/ul[5]/li[8]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/form/div/div/div[2]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/span[2]/input").send_keys("固定套餐一")
    # 输入活动名称
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/span[2]/input").send_keys("固定套餐一")
    time.sleep(2)
    #输入活动开始时间与活动结束时间
    driver.find_element_by_id("startDate").click()
    driver.find_element_by_id("laydate_today").click()
    time.sleep(2)
    driver.find_element_by_id("quitTimeChange3").click()
    time.sleep(2)
    #选择互斥活动
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[10]/div/div[1]/label/input").click()
    time.sleep(2)
    #添加商品
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[3]/div[1]/div[1]/div[2]").click()
    time.sleep(2)
    #选择商品
    driver.find_element_by_xpath("//table/tbody[1]/tr/td[1]/span/input").click()
    time.sleep(2)
    driver.find_element_by_xpath("//table/tbody[2]/tr/td[1]/span/input").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[8]/button").click()
    time.sleep(2)
    #拖动滚动条
    js="var q=document.documentElement.scrollTop=6000"
    driver.execute_script(js)
    # jsgo="srcollTo(0,10000)"
    # driver.execute_script(jsgo)
    time.sleep(2)
    #录入限购策略
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[3]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/select").click()
    time.sleep(2)
    driver.find_element_by_xpath("//select/option[3]").click()
    time.sleep(2)
    #录入套餐价格
    driver.find_element_by_xpath("//table/tbody[1]/tr/th[4]/span/input").send_keys('2')
    time.sleep(2)
    driver.find_element_by_xpath("//table/tbody[2]/tr/th[4]/span/input").send_keys('3')
    time.sleep(2)
    #保存方案
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[3]/div[2]/div[2]/button").click()
    time.sleep(5)
    #删除新增的固定套餐
    driver.find_element_by_xpath("//table/tbody/tr[1]/td[6]/span[2]/a").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/button[1]").click()
    time.sleep(5)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])#切换窗口，在新的窗口定位元素
    driver.close()