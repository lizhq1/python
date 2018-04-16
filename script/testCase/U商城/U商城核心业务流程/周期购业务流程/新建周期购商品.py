# coding=utf-8
import time

from selenium.webdriver import ActionChains
from time import sleep
import datetime, time, random
from selenium.webdriver.common.action_chains import ActionChains
import self

from SRC.common import utils_user

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from SRC.common import utils_user
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils


class EasyCase(TestCase):
    def get_goods_name(self):
        driver=self.getDriver()
        tool = utils_user
        test = tool.randomStr( 6, lowerCaseLetter=True, capitalLetter=True )
        goodsname="zhouqigou-"+test
        return goodsname
    def get_goods_code(self):
        driver=self.getDriver()
        tool = utils_user
        goodscode = tool.randomStr( 6, lowerCaseLetter=True, capitalLetter=True )
        return goodscode

    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        param = self.param

        #新增商品
        self.open_goods()
        goodscode=self.get_goods_code()
        goodsname=self.get_goods_name()
        print(goodsname)
        self.create_goods(goodscode,goodsname)
        self.select_goods_class()
        self.select_units()
        self.select_goods_style()
        # self.save_goods()
        self.grouding()


#打开商品新增界面
    def open_goods(self):
        driver=self.getDriver()
        driver.find_element_by_css_selector("div.col-xs-2.corp-mune.noprint > ul:nth-child(3) > li.title.pointer > upmark").click()  # 点击商品信息
        time.sleep(3)
        driver.find_element_by_css_selector("div.col-xs-2.corp-mune.noprint > ul:nth-child(3) > li:nth-child(2) > a").click()  # 点击商品列表
        time.sleep(3)
        driver.find_element_by_css_selector("div.row.m-t-20 > div.col-xs-6.text-right > a.btn.btn-warning.colorfff").click()  # 点击新增
        time.sleep(3)
        driver.find_element_by_css_selector('form > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > input').click()  # 选择普通商品
# 输入商品编码和名称
    def create_goods(self,goodscode,goodsname):
        driver=self.getDriver()
        driver.find_element_by_xpath('//input[@placeholder="必填"]').send_keys(goodscode)  # 输入商品编码“”
        time.sleep(3)
        driver.find_element_by_xpath('//input[@placeholder="最多可输入100个字符"]').send_keys(goodsname)  # 商品名称输入‘’
#选择商品分类
    def select_goods_class(self):
        driver=self.getDriver()
        driver.find_element_by_css_selector('form > div:nth-child(1) > div:nth-child(14) > div > div > div > div > input').click()#选择商品分类
        driver.find_element_by_css_selector('form > div:nth-child(1) > div:nth-child(14) > div > div > div > div > ul > li:nth-child(5)').click()#选择食品分类
#选择计量单位
    def select_units(self):
        driver=self.getDriver()
        dw=driver.find_element_by_xpath('//*[@id="dws"]')
        dw.find_element_by_xpath('//*[@id="dws"]/option[3]').click()  # 选择计量单位

        time.sleep(2)
#查询新增的商品
    def search(self,goodsname):
        driver=self.getDriver()
        driver.find_element_by_css_selector("div.col-xs-10.corp-content > div:nth-child(2) > div:nth-child(3) > div > div:nth-child(1) > div.row.space10 > div:nth-child(1) > div > input").send_keys(
            goodsname)  # 商品名称输入“”
        driver.find_element_by_xpath("//a[@ng-click='search()' and @class='btn btn-warning m-r-5']").click()  # 点击查询按钮
        time.sleep(5)

#保存商品
    def save_goods(self):
        driver=self.getDriver()
        driver.find_element_by_css_selector( '#editNavTab > div > button:nth-child(1)' ).click()  # 点击保存
        time.sleep(3)
#输入存量并且上架商品
    def grouding(self):
        driver=self.getDriver()
        js = "var q=document.body.scrollTop=2000"
        driver.execute_script( js )
        driver.find_element_by_css_selector("form > div:nth-child(1) > div:nth-child(23) > div.col-xs-5.p-l-0 > input").send_keys("12")
        time.sleep(2)
        driver.find_element_by_css_selector("form > div:nth-child(1) > div:nth-child(35) > div > input").send_keys("999")#输入现存量
        driver.find_element_by_css_selector("#editNavTab > div > button.btn.btn-default.m-l-4").click()
        time.sleep(3)
#选择商品类型
    def select_goods_style(self):
        driver=self.getDriver()
        time.sleep(2)
        select=driver.find_element_by_xpath("//form/div[1]/div[15]/div/select")
        options_list=select.find_elements_by_tag_name("option")
        count = 0
        for option in options_list:
             print ("Value is: " + option.get_attribute( "value" ))
             print("Text is:" + option.text)
             count = count + 1
             print(count)
        print(count)
        time.sleep(2)
        select.find_element_by_xpath("//form/div[1]/div[15]/div/select/option["+str(count)+"]").click()
        time.sleep(3)
