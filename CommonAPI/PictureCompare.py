#__author__ = 'Administrator'
# -*- coding:utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
from Config import Config as config
from CommonAPI import Adaptation

FalsePointList = [(-1L, -1L), (-1L, -1L), (-1L, -1L), (-1L, -1L), (-1L, -1L)]

def transfer_xy(centerlist, driver):
    w, h = Adaptation.getExecuteWH(driver)
    xtmp = int(centerlist[0][0])
    ytmp = int(centerlist[0][1])
    center_x = ytmp
    center_y = h - xtmp
    return center_x, center_y

def pointCompare(centerlist):
    for (x1, y1) in centerlist:
        for (x2, y2) in centerlist:
            if (x1-x2) > 5 or (y1 - y2) > 5:
                return False
    return True

def getScreenShot(driver, filename):
    filename = "Pictures/SrcImage/" + filename +'.jpg'
    driver.get_screenshot_as_file(filename)

def pictureCompare(srcName, dstName):
    centerlist = []
    srcPath = "Pictures/SrcImage/" + srcName
    dstPath = "Pictures/DstImage/" + dstName
    srcImage = cv2.imread(srcPath, 0)
    dstImage = cv2.imread(dstPath, 0)
    w,h = dstImage.shape[::-1]
    w1,h1 = srcImage.shape[::-1]
# 6 中匹配效果对比算法
    #methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']
    for meth in methods:
        method = eval(meth)
        res = cv2.matchTemplate(srcImage, dstImage, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        '''
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(srcImage,top_left, bottom_right, 255, 2)
        print meth
        plt.subplot(221), plt.imshow(srcImage,cmap= "gray")
        plt.title('Original Image'), plt.xticks([]),plt.yticks([])
        plt.subplot(222), plt.imshow(dstImage,cmap= "gray")
        plt.title('template Image'),plt.xticks([]),plt.yticks([])
        plt.subplot(223), plt.imshow(res,cmap= "gray")
        plt.title('Matching Result'), plt.xticks([]),plt.yticks([])
        plt.show()
        print(top_left)
        '''
        center = (top_left[0] + w/2, top_left[1] + h/2)
        centerlist.append(center)
        print(centerlist)
    if not pointCompare(centerlist):
        centerlist = FalsePointList
    return centerlist
