# 导入CV模块
import cv2 as cv


def face_detect_demo():
    gary = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # 根据本地文件进行分类器检查-人脸识别
    face_detect = cv.CascadeClassifier("F:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml")
    face = face_detect.detectMultiScale(gary)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv.imshow('result', img)


# 读取图片
img = cv.imread('5.jpg')

# 读取视频动态
mp4 = cv.VideoWriter()
# 检查函数
face_detect_demo()
# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break
# 释放摄像头
# mp4.release()
# 释放内存
cv.destroyAllWindows()

