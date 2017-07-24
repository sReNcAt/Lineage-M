# -*- coding: utf-8 -*-

'''
Require Modules

pip3 install numpy
pip3 install pyscreenshot
pip3 install pyautogui

OpenCV 3.2.0 and OpenCV Contrib 3.2.0

'''

import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pyautogui

import datetime
import time
import multiprocessing as mp
from multiprocessing import Process ,Queue
import os
import sys
import tkinter

return_town_x=0
return_town_y=0
attack_icon_x=1
attack_icon_y=2

class init():
    return_town_x=0
    return_town_y=0
    attack_icon_x=0
    attack_icon_y=0
    

class loop():
    loopbool=True

def mouse(x2,y2):
    init()
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    #pyautogui.moveTo(1080, 600)
    pyautogui.moveTo(x2,y2)
    
    #pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.moveTo(currentMouseX, currentMouseY)
    sys.exit()
    
def poison_mouse():
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(700, 600)
    #pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.moveTo(currentMouseX, currentMouseY)
    
def auto(q,x1,y1,x2,y2):
    if(loop.loopbool):
        pass
    else:
        return
    #img2 = np.array(ImageGrab.grab(bbox=(init.attack_icon_x,init.attack_icon_y,(init.attack_icon_x)+7,(init.attack_icon_y)+7)).convert('RGB'))
    img2 = np.array(ImageGrab.grab(bbox=(x1,y1,(x1)+3,(y1)+3)).convert('RGB'))
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    image2 = cv2.resize(img2,(6,6))
    #cv2.imshow('image',image2)
    #cv2.waitKey(0)
    temp=0
    tempbool=True
    for i in range(image2.shape[1]):
        #print(image2[0][i][2])
        if(image2[0][i][2]>220 and image2[0][i][1]>100 and image2[0][i][1]<150 and image2[0][i][0]>40 and image2[0][i][0]<80):
            temp+=1
        if(temp>4):
            tempbool=False
            break
    if(q.qsize()>0):
        loop.loopbool=False
        return
    if(tempbool):
        s = datetime.datetime.now()
        print(str(s)+" bypass")
        loop.loopbool=True
    else:
        s = datetime.datetime.now()
        print(str(s)+" return town")
        if(loop.loopbool==False):
            pass
        else:
            if(q.qsize()>0):
                loop.loopbool=False
            q.put("exit")
            #print('queue size')
            #print(q.qsize())
            mouse(x2,y2)
            loop.loopbool=False
        
    
    time.sleep(0.2)
def multi(q,x1,y1,x2,y2):
    
    while(loop.loopbool):
        #print('queue size')
        #print(q.qsize())
        if(loop.loopbool):
            pass
        else:
            q.put("exit")
        if(q.qsize()>0):
            break;
        auto(q,x1,y1,x2,y2)
    return
    
if __name__ == '__main__':
    init()
    #global return_town_x,return_town_y
    #global attack_icon_x,attack_icon_y
    print("귀환 주문서 버튼 위에 마우스를 올리시고 엔터를 눌러주세요.")
    input()
    return_town_x,return_town_y = pyautogui.position()
    print("공격버튼 정 중앙에 마우스를 올리시고 엔터를 눌러주세요.")
    input()
    attack_icon_x,attack_icon_y = pyautogui.position()
    attack_icon_x=attack_icon_x-3
    attack_icon_y=attack_icon_y-3
    print("귀환주문서 좌표")
    print("x : "+str(return_town_x)+"\ny : "+str(return_town_y))
    print("공격버튼 좌표")
    print("x : "+str(attack_icon_x)+"\ny : "+str(attack_icon_y))
    
    procs=[]
    q=Queue()
    for i in range(5):
        proc = Process(target=multi,args=(q,attack_icon_x,attack_icon_y,return_town_x,return_town_y,))
        procs.append(proc)
        proc.start()
        time.sleep(0.25)
    for proc in procs:
        proc.join()
        time.sleep(0.25)
