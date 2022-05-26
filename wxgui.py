# 微信自动登录发送消息

import time
import pyautogui
import pyperclip
import os
import random


def mapping_img(img, click):
    box_location = pyautogui.locateOnScreen(img, confidence=0.9)
    center = pyautogui.center(box_location)
    if click == 'double':
        pyautogui.doubleClick(center)
    else:
        pyautogui.leftClick(center)
    time.sleep(1)


def chat_user(user):
    if user != '':
        mapping_img('search.png', 'single')
        pyautogui.typewrite(user)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.moveRel(xOffset=0, yOffset=130)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
    else:
        mapping_img('wode.png', 'single')
        time.sleep(1)
        mapping_img('chat.png', 'single')


def read_txt(txt):
    hellofile = open(txt, "r", encoding="UTF-8")
    hellocontent = hellofile.readline()
    print(len(hellocontent))
    number = random.randint(0, len(hellocontent) - 1)
    print('line number is {}'.format(number))
    pyperclip.copy(hellocontent)
    pyautogui.hotkey('ctrl', 'v')
    hellofile.close()


def read_img(img_name):
    mapping_img('pic.png', 'single')
    img_path = 'c:\\Users\\zhusd\\Desktop\\autopygui\\' + img_name
    pyautogui.typewrite(img_path)
    pyautogui.press('enter')


def main():
    os.chdir('c:/Users/zhusd/Desktop/autopygui')
    print(os.getcwd())
    # TOOO login wechat
    mapping_img('login.png', 'double')
    time.sleep(1)
    # TOOO search chat user
    chat_user('bengtua')
    time.sleep(1)
    # TOOO start chatting
    read_txt('hello.txt')
    pyautogui.press('enter')
    time.sleep(1)
    read_txt('yulu.txt')
    pyautogui.press('enter')
    time.sleep(1)
    read_img('zhenni.png')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    # mapping_img('send.png', 'single')
    time.sleep(1)


if __name__ == '__main__':
    main()
