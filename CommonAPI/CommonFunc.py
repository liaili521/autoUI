#__author__ = 'Administrator'
# -*- coding:utf-8 -*-

from appium import webdriver
from CommonAPI import PictureCompare as pc
from CommonAPI import ElementOperate as eo
from CommonAPI import Adaptation as adpt
import logging
import traceback
from Config import Config as config
import time

def startLanch(driver):
    #启动wetest
    '''
    driver.find_element_by_id("com.tencent.wefpmonitor:id/generic_layout").click()
    resource_id = "com.tencent.wefpmonitor:id/okbutton"
    if eo.waitElementById(driver, resource_id):
        driver.find_element_by_id(resource_id).click()
    resource_id = "com.tencent.wefpmonitor:id/btnstart"
    if eo.waitElementById(driver, resource_id):
        driver.find_element_by_id(resource_id).click()
    '''
    #点击确认按钮
    '''
    try:
        time.sleep(3)
        exew , exeh = adpt.getExecuteWH(driver)
        exewh = (exew, exeh)
        driver.tap([adpt.exeAdaption(config.loadingok[0], config.loadingok[1], exewh)], 100)
    except:
        print traceback.format_exc()
    '''
    try:
        time.sleep(3)
        exew , exeh = adpt.getExecuteWH(driver)
        exewh = (exew, exeh)
        print(exewh)
        driver.tap([adpt.exeAdaption(config.selectenv[0], config.selectenv[1], exewh)], 100)
    except:
        print traceback.format_exc()
    for i in range(0,10):
        print(i)
        time.sleep(2)
        pc.getScreenShot(driver, "screenshot")
        centerlist = pc.pictureCompare("screenshot.jpg", "temp_notify_19201080.jpg")
        if centerlist[0] != (-1, -1):
            driver.tap([adpt.exeAdaption(config.tempclose[0], config.tempclose[1], exewh)], 100)
            break
    for i in range(0,10):
        print(i)
        time.sleep(2)
        pc.getScreenShot(driver, "screenshot")
        centerlist = pc.pictureCompare("screenshot.jpg", "start_icon_19201080.jpg")
        if centerlist[0] != (-1, -1):
            center_x, center_y = pc.transfer_xy(centerlist, driver)
            driver.tap([(center_x, center_y)], 100)
            break
    time.sleep(2)
    driver.tap([adpt.exeAdaption(960, 540, exewh)], 100)
    driver.tap([adpt.exeAdaption(960, 540, exewh)], 100)
    time.sleep(5)

def exeCmd(driver):
    exew , exeh = adpt.getExecuteWH(driver)
    exewh = (exew, exeh)
    driver.tap([adpt.exeAdaption(config.cmdbutton[0], config.cmdbutton[1], exewh)], 100)
    time.sleep(0.5)
    driver.tap([adpt.exeAdaption(config.cmdtext[0], config.cmdtext[1], exewh)], 100)
    time.sleep(0.5)
    driver.find_element_by_class_name("android.widget.EditText").send_keys("$autoBattle")
    driver.find_element_by_class_name("android.widget.Button").click()
    time.sleep(0.5)
    driver.tap([adpt.exeAdaption(config.cmdok[0], config.cmdok[1], exewh)], 100)
    time.sleep(0.5)
    driver.tap([adpt.exeAdaption(config.cmdbutton[0], config.cmdbutton[1], exewh)], 100)
    time.sleep(1)

def closeWetest(driver):
    exew , exeh = adpt.getExecuteWH(driver)
    exewh = (exew, exeh)
    driver.tap([adpt.exeAdaption(config.wetestclose[0], config.wetestclose[1], exewh)], 100)
    time.sleep(0.5)
    driver.find_element_by_id("com.tencent.wefpmonitor:id/okbutton").click()
    resource_id = "com.tencent.wefpmonitor:id/T_btnSave"
    if eo.waitElementById(driver, resource_id):
        driver.find_element_by_id(resource_id).click()
    #driver.close_app();
