# coding=utf-8

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
from SRC.common import utils_user
import time,random,datetime


class EasyCase(TestCase):
    def __init__(self, webDriver,paramsList):
    # 请不要修改该方法
        super(EasyCase, self).__init__(webDriver,paramsList)
    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        tool = utils_user
        # goodsname = tool.randomStr( 6, lowerCaseLetter=True, capitalLetter=True )
        self.select_goods()#模糊查询周期购的商品
        self.select_dispatching_shop()#选择按照门店配送
        self.dispatching_time(self.judge_times_style())#录入或者选择配送时长
        self.dispatching_everymuch(self.judge_everymuch_style())#录入或者选择每次配送量
        self.every_time_date(self.judge_cycle())#选择配送日（每周一次，每月一次或者按日配送）
        self.select_detail_startdate()#选择输入开始配送日期
        self.submit_order()#提交订单，填写配送时间
        self.pay_order()#储值卡支付订单
        self.search_order()#查询支付的订单
        self.brower_dispathing()#查看配送计划



    #用于判断商品界面配送时长是输入还是参照选择的
    def judge_times_style(self):
        driver=self.getDriver()
        span_content=driver.find_element_by_css_selector("#cyclePurchase-select > ul > li:nth-child(1) > div").findall("span")
        if span_content.len()==0:
            fag="input"
            return fag
        elif span_content.len()>0:
            fag="select"
            return fag
    #用于判断商品界面每次配送量是输入还是参照选择的
    def judge_everymuch_style(self):
        driver=self.getDriver()
        # js="$ var $div=$(\"#cyclePurchase-select > ul > li:nth-child(2) > div\");span_content=$div.children('span').len()"
        # driver.execute_script( js )
        span_content=driver.find_element_by_css_selector("#cyclePurchase-select > ul > li:nth-child(2) > div").find_all("span")
        if span_content.len()==0:
            fag="input"
            return fag
        elif span_content.len()>0:
            fag="select"
            return fag
    #用于判断商品的配送周期是什么，根据界面显示的文字，来判断；
    def judge_cycle(self):
        driver=self.getDriver()
        context=driver.find_element_by_css_selector("#cyclePurchase-select > ul > li:nth-child(1) > span > i").text
        if context=="(每周一次)":
            fag="week"
            return fag
        elif context=="(每月一次)":
            fag="month"
            return fag
        elif context=="(按日配送)":
            fag="day"
            return fag
#搜索商品
    def select_goods(self):
        driver=self.getDriver()
        driver.find_element_by_css_selector('#search > div > div.search_box_t > div > input[type="text"]').clear()
        driver.find_element_by_css_selector('#search > div > div.search_box_t > div > input[type="text"]').send_keys("zhouqigou-")  # 在搜索栏输入模糊查询周期购的商品
        driver.find_element_by_css_selector('#search > div > div.search_box_t > a > i').click()  # 点击搜索
        time.sleep(3)
#选择商品，选择按照门店配送
    def select_dispatching_shop(self):
        driver=self.getDriver()
        driver.find_element_by_xpath("//div/div[4]/div/div[3]/ul/li/div/div[1]/a/img").click()
        driver.switch_to_window( driver.window_handles[1] )
        time.sleep(3)
        #driver.find_element_by_css_selector("body > div.container.bg-fa > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div > div.pays_list.orderExpress > div.distributionInfo > div:nth-child(10)").click()
        driver.find_element_by_css_selector("#skus-select > ul > li > div > span:nth-child(3)").click()
        time.sleep(3)

#按日配送，选择开始配送日期，从当前日期开始的第三天开始配送
    def select_detail_startdate(self):
        driver=self.getDriver()
        today = datetime.date.today()
        startdate=today+datetime.timedelta(days=2)#从当前日期开始计算，最近的开始配送日期为2天以后
        driver.find_element_by_css_selector("#cyclePurchase-select > ul > li:nth-child(4) > div > input").click()
        print(startdate)
        driver.find_element_by_css_selector( "#cyclePurchase-select > ul > li:nth-child(4) > div > input" ).send_keys(str(startdate))
        time.sleep(3)
#输入配送的信息或者选择配送的信息，配送次数和配送量
    def dispatching_time(self,sign1):
        driver = self.getDriver()
        if sign1=="input":
            days=random.randint(1,10)#随机生成配送天数并输入
            driver.find_element_by_xpath( "//div[2]/ul/li[1]/div/input" ).send_keys( days )
        elif sign1=="select":
            driver = self.getDriver()
            i = random.randint( 1, 4 )#随机生成配送天数并选择
            driver.find_element_by_xpath( "//div[2]/ul/li[1]/div/span["+str(i)+"]" ).click()
#输入或者参照每次配送量
    def dispatching_everymuch(self,sign2):
        driver = self.getDriver()
        if sign2 == "input":
            everymuch = random.randint( 1, 3 )  # 随机生成每次配送的量并输入
            driver.find_element_by_xpath( "//div[2]/ul/li[2]/div/input" ).send_keys( everymuch )
        elif sign2=="select":
            j = random.randint( 1, 5 )  # 随机生成每次配送的量并选择
            driver.find_element_by_xpath( "//div[2]/ul/li[2]/div/span["+str(j)+"]" ).click()
# #选择录入配送频次
#     def dispatching_rate(self,sign3):
#         driver = self.getDriver()
#         if sign3=="input":
#             k = random.randint( 1, 5 )
#             driver.find_element_by_xpath( "//div[2]/ul/li[3]/div/span["+str(k)+"]" ).click()
#选择配送周期，与商品档案中商品类型设置的周期购信息须一致
    def every_time_date(self,fag):
        driver=self.getDriver()
        if fag=="day":#按日配送
            i=random.randint(1,5)#(每天送、隔天送、工作日送、双休日送)随机选择一种
            driver.find_element_by_css_selector("#cyclePurchase-select > ul > li:nth-child(3) > div > span:nth-child("+str(i)+")").click()
        elif fag=="week":#每周一次
            i=random.randint(1,7)#一周七天，随机选择一天
            driver.find_element_by_css_selector("#cyclePurchase-select > ul > li:nth-child(3) > div > span:nth-child("+str(i)+")").click()
        elif fag=="month":#每月一次
            i=random.randint(1,30)#一个月30天，随机选择一天
            driver.find_element_by_css_selector("#cyclePurchase-select > ul > li:nth-child(3) > div > span:nth-child("+str(i)+")").click()
    #提交订单
    def submit_order(self):
        driver=self.getDriver()
        driver.find_element_by_xpath("//div/div[2]/div[4]/div[4]/a[1]/span").click()
        time.sleep(5)
        driver.find_element_by_css_selector("body > div.container.bg-fa > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div > div.pays_list.orderExpress > div.distributionInfo > div:nth-child(10) > select").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div > div.pays_list.orderExpress > div.distributionInfo > div:nth-child(10) > select > option:nth-child(5)").click()
        time.sleep(5)
        js2= "var q=document.body.scrollTop=2000"#拖动滚动条
        driver.execute_script( js2 )
        driver.find_element_by_css_selector("body > div.container.bg-fa > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div > div.osubmit > div > button").click()
        time.sleep(4)
    #支付订单
    def pay_order(self,fag):
        driver=self.getDriver()
        driver.find_element_by_css_selector("#body1 > dl > dd:nth-child(2) > ul > li:nth-child(4) > div:nth-child(1) > input").click()
        driver.find_element_by_class_name("btnPayment").click()
        if fag=="true":
            driver.find_element_by_css_selector("#password0").send_keys("111111")
            driver.find_element_by_css_selector("#confirmPayBtn").click()
            time.sleep(5)
    def search_order(self):
        driver=self.getDriver()
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/span[2]/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div/div[5]/div[1]/div/div/ul/li[4]/ul/li[1]/a/span").click()
        #搜索订单
        driver.find_element_by_css_selector( '#startDate' ).click()
        driver.find_element_by_css_selector( '#laydate_today' ).click()
        driver.find_element_by_css_selector( '#endDate' ).click()
        driver.find_element_by_css_selector( '#laydate_today' ).click()
        # 点击搜索
        driver.find_element_by_css_selector( '#ordersearch' ).click()
    def brower_dispathing(self):
        driver=self.getDriver()
        driver.find_element_by_xpath("//table/tbody/tr[2]/td[8]/div[3]/a")



