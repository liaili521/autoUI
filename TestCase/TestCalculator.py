#__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import unittest
from appium import webdriver
from CommonAPI import PictureCompare as pc
import logging
from CommonAPI import InteracrionADB as op_adb
import datetime
import subprocess
import time
import os

class TestCalulator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        try:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            #desired_caps['deviceName'] = 'QKCM7SIVAMEAYP6P'
            #desired_caps['deviceName'] = '75UBBLE224SW'
            desired_caps['deviceName'] = 'XGC4C16513019403'
            desired_caps['appPackage'] = 'com.android.calculator2'
            desired_caps['appActivity'] = '.Calculator'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        except:
            self.driver.quit()

    def saveClientLog(self, str):
        target_pid = op_adb.findPid(str)
        print(type(target_pid))
        print(target_pid)
        timezone = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        logname = "client_logcat" + timezone + ".txt"
        self.logcat_file = open(logname, 'w')
        #logcmd = "adb logcat -v time | findstr 1127"
        #logcmd = "adb logcat -v time"
        logcmd_tmp = "adb logcat -v time | findstr "  + target_pid
        logcmd = logcmd_tmp
        print(logcmd)
        #logcmd = "adb logcat -v time"
        self.Poplog = subprocess.Popen(logcmd,shell=True, stdout=self.logcat_file, stderr=subprocess.PIPE)

    def testAdd(self):
        self.saveClientLog("com.android.calculator2")
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
        self.logcat_file.close()
        self.Poplog.terminate()


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        os.system('taskkill /f /t /im adb.exe')#关闭所有adb进程



