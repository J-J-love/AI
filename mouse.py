import pyautogui
import time

pyautogui.FAILSAFE = False
# 设置鼠标的起始位置
start_x, start_y = pyautogui.position()

# 设置鼠标要移动到的目标位置
target_x = 10
target_y = 10

# 设置移动时间（秒）
duration = 1

# 计算每秒移动的像素数
distance_x = target_x - start_x
distance_y = target_y - start_y

# 计算每0.1秒的速度
x_speed = distance_x / (duration * 10)
y_speed = distance_y / (duration * 10)

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
pyautogui.click(target_x,target_y)