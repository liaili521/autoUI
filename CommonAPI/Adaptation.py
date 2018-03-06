#__author__ = 'Administrator'
# -*- coding:utf-8 -*-
import logging
from Config import Config as config

def getExecuteWH(driver):
    execute_width = driver.get_window_size()['width']
    execute_height = driver.get_window_size()['height']
    logging.info("The executing phone: width is " + str(execute_width) + " height is " + str(execute_height))
    return execute_width, execute_height

def exeAdaption(coordinateX, coordinateY , exewh):
    execute_x = coordinateX * exewh[0] / config.Resolution_base[0]
    execute_y = coordinateY * exewh[1] / config.Resolution_base[1]
    return execute_x, execute_y


