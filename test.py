from selenium import webdriver
def open(url):
    driver=webdriver.Firefox()
    driver.get(url)
open('http://www.baidu.com')
