#__author__ = 'Administrator'
# -*- coding:utf-8 -*-
from appium import webdriver
from CommonAPI import PictureCompare as pc
from TestCase import TestWeTest
from TestCase import TestCalculator
from TestCase import TestScreenShot
import logging
import unittest

allcase='E:\\AutoUI\TestCase'     #指明要自动查找的py文件所在文件夹路径

#添加每个module里面单独的测试用例
def getTestSuite1():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator.TestCalulator("testAdd"))
    #suite.addTest(TestWeTest.TestWeTest("testStreet"))
    #suite.addTest(TestScreenShot.TestScreenShot("testScreenShot"))
    return suite

#以module作为执行单元
def getTestSuite2():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestWeTest.TestWeTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCalculator.TestCalulator)
    suite = unittest.TestSuite([suite1,suite2])
    return suite

#执行一个目录下所有以.py结尾的测试用例
def getTestSuit3():
    testunit = unittest.TestSuite()
    #使用discover找出用例文件夹下test_casea的所有用例
    discover=unittest.defaultTestLoader.discover(allcase,                             #查找的文件夹路径
    pattern='Test*.py',                                                             #要测试的模块名，以start开头的.py文件
    top_level_dir=None)                                                               #测试模块的顶层目录，即测试用例不是放在多级目录下，设置为none
    for suite in discover:  #使用for循环出suite,再循环出case
        for case in suite:
            testunit.addTests(case)
            print testunit
    return testunit

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
    runner = unittest.TextTestRunner()
    suite = getTestSuite1()
    runner.run(suite)

    #centerlist = pc.pictureCompare("screenshot.jpg", "start_icon.jpg")


