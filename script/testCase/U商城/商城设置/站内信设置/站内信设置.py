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

        self.open()
        self.addusers()

    #打开站内信设置菜单
    def open(self):
        driver=self.getDriver()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[8]/li[1]/upmark").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/ul[8]/li[5]/a").click()
        time.sleep( 5 )

    def addusers(self):
        driver=self.getDriver()
        for i in range(1,6):
        #js1 = "var $td = $(\"tr:nth-child(1) > td:nth-child(3)\");var $ele = $td.children('span').last().prev();$ele.click()"
        # js1="var $ele=table > tbody > tr:nth-child(1) > td:nth-child(3)> span:nth-last-child(3);$ele.click()"
            print(i)
            driver.find_element_by_css_selector( "table > tbody > tr:nth-child("+str(i)+") > td:nth-child(3)> span:nth-last-child(3)").click()
            time.sleep(2)
            driver.find_element_by_css_selector(" table > tbody > tr:nth-child("+str(i)+") > td:nth-child(3) > div > div > span > i").click()
            time.sleep( 2 )
            driver.find_element_by_css_selector("#ui-select-choices-row-"+str(i-1)+"-0 > a").click()
            time.sleep( 2 )
            driver.find_element_by_css_selector("table > tbody > tr:nth-child("+str(i)+") > td:nth-child(3) > button").click()
            time.sleep(3)
            driver.find_element_by_css_selector( "table > tbody > tr:nth-child("+str(i)+") > td:nth-child(3)> span:nth-last-child(5)").click()
            driver.find_element_by_css_selector(" table > tbody > tr:nth-child("+str(i )+") > td:nth-child(3) > span:nth-child(1) > span.close.ui-select-match-close" ).click()
        driver.find_element_by_css_selector(" div:nth-child(3) > div > button").click()
        time.sleep( 5 )
        driver.find_element_by_xpath( "/html/body/div[1]/div[1]/div/div[1]/ul[8]/li[1]/upmark" ).click()

        # driver.execute_script( js1 )
