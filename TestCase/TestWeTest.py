#__author__ = 'Administrator'
# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from CommonAPI import PictureCompare as pc
from CommonAPI import ElementOperate as eo
from CommonAPI import CommonFunc as cf
from CommonAPI import Adaptation as adpt
import logging
import traceback
from Config import Config as config
import time

class TestWeTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        try:
            '''
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'QKCM7SIVAMEAYP6P'
            #desired_caps['deviceName'] = '75UBBLE224SW'
            desired_caps['appPackage'] = 'com.tencent.wefpmonitor'
            desired_caps['appActivity'] = 'com.tencent.cube.activity.WelcomePageActivity'
            desired_caps['newCommandTimeout'] = '300'
            desired_caps['appWaitActivity'] = 'com.tencent.WTMainActivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
           '''
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'QKCM7SIVAMEAYP6P'
            #desired_caps['deviceName'] = '75UBBLE224SW'
            desired_caps['appPackage'] = 'com.tencent.kof'
            desired_caps['appActivity'] = 'com.tencent.tmgp.kof.GameActivity'
            desired_caps['newCommandTimeout'] = '300'
            #desired_caps['appWaitActivity'] = 'com.tencent.WTMainActivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        except:
            print traceback.format_exc()

    def testStreet(self):
        cf.startLanch(self.driver)
        cf.exeCmd(self.driver)
        exew , exeh = adpt.getExecuteWH(self.driver)
        exewh = (exew , exeh)
        self.driver.tap([adpt.exeAdaption(config.challenge_icon[0], config.challenge_icon[1], exewh)], 100)
        time.sleep(2)
        self.driver.tap([adpt.exeAdaption(config.street_icon[0], config.street_icon[1], exewh)], 100)
        time.sleep(2)
        self.driver.tap([adpt.exeAdaption(config.street_challenge[0][0], config.street_challenge[0][1], exewh)], 100)
        time.sleep(2)
        self.driver.tap([adpt.exeAdaption(config.street_start[0], config.street_start[1], exewh)], 100)
        time.sleep(55)
        for i in range(0,10):
            print(i)
            time.sleep(2)
            pc.getScreenShot(self.driver, "screenshot")
            centerlist = pc.pictureCompare("screenshot.jpg", "street_win_19201080.jpg")
            centerlist1 = pc.pictureCompare("screenshot.jpg", "street_lose_19201080.jpg")
            if centerlist[0] != (-1, -1):
                self.driver.tap([adpt.exeAdaption(config.back_city[0], config.back_city[1], exewh)], 100)
                break
            if centerlist1[0] != (-1, -1):
                self.driver.tap([adpt.exeAdaption(config.back_city[0], config.back_city[1], exewh)], 100)
                break
        time.sleep(20)
        #cf.closeWetest(self.driver)

    '''
    def testLancher(self):
        exew , exeh = adpt.getExecuteWH(self.driver)
        exewh = (exew , exeh)
        self.driver.find_element_by_id("com.tencent.wefpmonitor:id/generic_layout").click()
        resource_id = "com.tencent.wefpmonitor:id/okbutton"
        if eo.waitElementById(self.driver, resource_id):
            self.driver.find_element_by_id(resource_id).click()
        resource_id = "com.tencent.wefpmonitor:id/btnstart"
        if eo.waitElementById(self.driver, resource_id):
            self.driver.find_element_by_id(resource_id).click()
        try:
            time.sleep(2)
            self.driver.tap([adpt.exeAdaption(config.loadingok[0], config.loadingok[1], exewh)], 100)
        except:
            print traceback.format_exc()
        for i in range(0,6):
            print(i)
            time.sleep(3)
            pc.getScreenShot(self.driver, "screenshot")
            centerlist = pc.pictureCompare("screenshot.jpg", "start_icon_19201080.jpg")
            if centerlist[0] != (-1, -1):
                center_x, center_y = pc.transfer_xy(centerlist, self.driver)
                print(center_x, center_y)
                self.driver.tap([(center_x, center_y)], 100)
                break
        time.sleep(5)

    def testCmd(self):
        exew , exeh = adpt.getExecuteWH(self.driver)
        exewh = (exew , exeh)
        self.driver.tap([adpt.exeAdaption(config.cmdbutton[0], config.cmdbutton[1], exewh)], 100)
        time.sleep(0.5)
        self.driver.tap([adpt.exeAdaption(config.cmdtext[0], config.cmdtext[1], exewh)], 100)
        time.sleep(0.5)
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("$autoBattle")
        self.driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(0.5)
        self.driver.tap([adpt.exeAdaption(config.cmdok[0], config.cmdok[1], exewh)], 100)
        time.sleep(0.5)
        self.driver.tap([adpt.exeAdaption(config.cmdbutton[0], config.cmdbutton[1], exewh)], 100)
        time.sleep(0.5)

    def testClose(self):
        exew , exeh = adpt.getExecuteWH(self.driver)
        exewh = (exew , exeh)
        self.driver.tap([adpt.exeAdaption(config.wetestclose[0], config.wetestclose[1], exewh)], 100)
        time.sleep(0.5)
        self.driver.find_element_by_id("com.tencent.wefpmonitor:id/okbutton").click()
        resource_id = "com.tencent.wefpmonitor:id/T_btnSave"
        if eo.waitElementById(self.driver, resource_id):
            self.driver.find_element_by_id(resource_id).click()
        self.driver.close_app();
        '''

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
