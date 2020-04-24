import pyautogui
import pygame
import time


pygame.init()
cnt=0
x_old=0;y_old=0;
while True:
    tmp = pyautogui.position()
    if x_old == tmp.x and y_old == tmp.y:
        cnt+=1
    else :
        cnt=0
    if cnt == 5:
        print("CHECK!!!  x : " + str(tmp.x) + " y : "+str(tmp.y))
        break
    x_old = tmp.x;y_old = tmp.y;
    time.sleep(1)


pyautogui.click(x_old,y_old)


print("Current Mouse Position : ",pyautogui.position())

#pyautogui.click(104.594,button='left',clicks=1,interval = 1)