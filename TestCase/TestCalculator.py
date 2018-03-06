#__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import unittest
from appium import webdriver
from CommonAPI import PictureCompare as pc
import logging

class TestCalulator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        try:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'QKCM7SIVAMEAYP6P'
            #desired_caps['deviceName'] = '75UBBLE224SW'
            desired_caps['appPackage'] = 'com.android.calculator2'
            desired_caps['appActivity'] = '.Calculator'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        except:
            self.driver.quit()

    def testAdd(self):
        self.driver.find_element_by_id("com.android.calculator2:id/digit5").click()
        self.driver.find_element_by_id("com.android.calculator2:id/digit1").click()
        self.driver.find_element_by_id("com.android.calculator2:id/digit9").click()
        self.driver.find_element_by_id("com.android.calculator2:id/del").click()
        self.driver.find_element_by_id("com.android.calculator2:id/digit9").click()
        self.driver.find_element_by_id("com.android.calculator2:id/digit5").click()
        self.driver.find_element_by_id("com.android.calculator2:id/plus").click()
        self.driver.find_element_by_id("com.android.calculator2:id/digit6").click()
        self.driver.find_element_by_id("com.android.calculator2:id/equal").click()
        pc.getScreenShot(self.driver, "test")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

