# coding=utf-8
from time import sleep
import datetime, time, random
from SRC.common import utils_user

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase


class EasyCase(TestCase):
    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):

        driver = self.getDriver()
        tool = utils_user
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        # self.log_combo_set()
        self.open()
        self.select_check("NewCheck")
        self.select_is("//form/div[2]/div/div")
        self.select_is("//form/div[3]/div/div")
        self.select_is("//form/div[4]/div/div")
        self.select_is("//form/div[5]/div/div")
        self.select_is("//form/div[6]/div/div")
        self.select_settlement("diffPrice")
        self.select_is("//form/div[9]/div/div")
        self.select_bill("supplier")
        self.save()


    def open(self):
        driver = self.getDriver()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[7]/li[1]/upmark").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[7]/li[2]/a").click()
        time.sleep(2)
        # 供应商商品是否需要审核后才能上架


    def select_check(self, fag):
        driver = self.getDriver()
        if fag == "NotCheck":
            if not driver.find_element_by_xpath("//form/div[1]/div/input[1]").is_selected():
                driver.find_element_by_xpath("//form/div[1]/div/input[1]").click()
        elif fag == "NewCheck":
            if not driver.find_element_by_xpath("//form/div[1]/div/input[2]").is_selected():
                driver.find_element_by_xpath("//form/div[1]/div/input[2]").click()
        elif fag == "NewNotCheck":
            if not driver.find_element_by_xpath("//form/div[1]/div/input[3]").is_selected():
                driver.find_element_by_xpath("//form/div[1]/div/input[3]").click()
        # 判断是否选择


    def select_is(self, xpath):
        driver = self.getDriver()
        if driver.find_element_by_xpath(xpath).get_attribute("class") == "pValid-false":
            driver.find_element_by_xpath(xpath).click()
        # 供应商结算方式


    def select_settlement(self, fag):
        driver = self.getDriver()
        if fag == "keepSettlement":
            if not driver.find_element_by_xpath("//form/div[8]/div/input[1]").is_selected():
                driver.find_element_by_xpath("//form/div[8]/div/input[1]").click()
        if fag == "diffPrice":
            if not driver.find_element_by_xpath("//form/div[8]/div/input[2]").is_selected():
                driver.find_element_by_xpath("//form/div[8]/div/input[2]").click()
        #供应商开票方式
    def select_bill(self,fag):
        driver=self.getDriver()
        if fag=="plat":
            driver.find_element_by_xpath("//form/div[10]/div/input[1]").click()
        elif fag=="supplier":
            driver.find_element_by_xpath("//form/div[10]/div/input[2]").click()
        #保存供应商设置
    def save(self):
        driver=self.getDriver()
        driver.find_element_by_xpath("//form/div[11]/div/button").click()
        time.sleep(3)
