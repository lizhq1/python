from selenium import webdriver
def login(self,usename,password,sign):
	driver=self.driver
	driver.find_element_by_name('uname').send_keys('usename')
	driver.find_elemnet_by_name('password').send_keys('password')
	driver.find_element_by_name('signupverifycode').send_key('sign')
	driver.find_element_by_link_text('登陆').click()
