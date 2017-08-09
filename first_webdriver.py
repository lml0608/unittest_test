# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from selenium import webdriver

import os


import unittest

import HTMLTestRunner

import time


class BaiduTest(unittest.TestCase):

    def setUp(self):


        self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(30)

        self.base_url = "http://wwww.baidu.com"



    def test_baidu_search(self):


        driver = self.driver

        driver.get(self.base_url)


        self.assertEqual(driver.title,"百度一下，你就知道")


        driver.find_element_by_id("kw").clear()

        driver.find_element_by_id("kw").send_keys("selenium")

        driver.find_element_by_id("su").click()

        time.sleep(3)

        self.assertEqual(driver.title,"selenium_百度搜索")



    def tearDown(self):

        self.driver.quit()



if __name__=="__main__":


    #定义测试套件集
    testunit = unittest.TestSuite()

    #将用例加入的套件中
    testunit.addTest(BaiduTest('test_baidu_search'))


    htmlpath = "D:\\dev\\unittest_test\\testReport.html"

    print(os.path.abspath(htmlpath))

    fp = open(htmlpath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="ceshi",
                                           description="report")


    runner.run(testunit)

    fp.close()











