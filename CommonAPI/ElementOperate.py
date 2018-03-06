#__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import time
import traceback
import logging

def waitElementById(driver, resource_id):
    time.sleep(1)
    try:
         if driver.find_element_by_id(resource_id).is_displayed():
             return True
         else:
             return False
    except:
        logging.info(traceback.format_exc())

def waitElementByName(driver, name):
    time.sleep(1)
    try:
         if driver.find_element_by_name(name).is_displayed():
             return True
         else:
             return False
    except:
        logging.info(traceback.format_exc())

def waitElementByClassName(driver, classname):
    time.sleep(1)
    print("waitElementByClassName")
    try:
         if driver.find_element_by_class_name(classname).is_displayed():
             return True
         else:
             return False
    except:
        logging.info(traceback.format_exc())
