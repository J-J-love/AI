import pyautogui
import time
from datetime import datetime, timedelta
import keyboard
import random
# 1、实现图像检测目标 2、把目标对象的坐标实时的获取到 3、把对象的坐标用列表存储起来 4、通过判断列表下的下标是否为0判断消灭怪物 5、根据列表中的对象获取到的离主角最近的怪物坐标进行消灭

def mouse():
    pyautogui.FAILSAFE = False
    # 设置鼠标的起始位置
    start_x, start_y = pyautogui.position()
    # 设置鼠标点击间隔
    interval = 0.1
    # 设置鼠标要移动到的目标位置
    target_x = 1356
    target_y = 766

    # 设置移动时间（秒）
    duration = 1

    # 计算每秒移动的像素数
    distance_x = target_x - start_x
    distance_y = target_y - start_y

    # 计算每0.1秒的速度
    x_speed = distance_x / (duration * 1)
    y_speed = distance_y / (duration * 1)

    # 开始移动鼠标
    start_time = time.time()
    while time.time() - start_time < duration:
        current_x, current_y = pyautogui.position()
        # 计算下一个位置
        next_x = current_x + x_speed
        next_y = current_y + y_speed
        # 移动鼠标到下一个位置
        pyautogui.moveTo(next_x, next_y, duration=0)

    # 将鼠标移动到目标位置，以确保准确性
    pyautogui.moveTo(target_x, target_y, duration=0.5)

    # 最后点击鼠标左键

    # 设置鼠标点击次数
    clicks = 100
    for i in range(clicks):
        time.sleep(0.1)
        pyautogui.click(target_x, target_y)
        pyautogui.doubleClick(target_x, target_y)


def mouse_click():
    exit_keys = "q"
    time1 = [100, 1]
    time2 = 0
    for i in range(0, len(time1)):
        if keyboard.is_pressed(exit_keys):
            break
        elif time1[i] < time2:
            return
        else:
            mouse()


mouse_click()
