#__author__ = 'Administrator'
import os
import re
import subprocess
import time
import datetime

'''
out1 = os.popen('adb devices').read()
print(out1)
'''

def interactADB(str):
    os.system(str)

def findPid(str):
    cmds = [
        "ps | grep " + str,
        "exit",#important
    ]
    pipe = subprocess.Popen("adb shell", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out2 = pipe.communicate("\n".join(cmds) + "\n");
    print(out2)
    out3 = out2[0].split("\r\r\n")
    print(out3)
    for i in range(0,len(out3)):
        if not "ps | grep" in out3[i]:
            if out3[i].endswith(str):
                out4 = out3[i].split(" ")
                for i in out4:
                    if "" in out4:
                        out4.remove("")
    print(out4[1])
    return out4[1]





