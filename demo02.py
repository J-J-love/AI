# 导入CV模块
import cv2 as cv

# 读取图片
img = cv.imread('1.png')
# 灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# 显示灰度
cv.imshow('gray', gray_img)
# 显示图片
cv.imshow('demoImg', img)
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()
