# -*- coding: utf-8 -*-
import random

import decimal

# 随机数重现
state = random.getstate()
print('number1', [random.randint(1, 10) for i in range(5)])

random.setstate(state)
print('number2', [random.randint(1, 10) for i in range(5)])

# 浮点数
number1 = decimal.Decimal('0.1')
number2 = decimal.Decimal('0.2')
print(number1 + number2)

print(float(1 * decimal.Decimal('0.1')))

# 复数的计算方式
a = complex(2, 2)
b = complex(1, 2)
print(a - b)

# x+y x-y x*y x/y
# x//y x%y -x +x
# abs(x) int(x) float(x) complex(re,im)
# c.conjugate() divmod(x,y) pow(x,y) x ** y

# 获取组件名
print(input.__name__)


# 定义函数
def hello():
    print('你好', end='')


def hello1():
    hello()
    print('俊杰')


hello1()


# 带参函数
def demo01(width, high: int):
    """测试显示提示信息"""
    print(width * high)


demo01(5, 10)

demo01(10, 10)


# 调用函数返回值
def demo02(aa, bb): 
    aa = bb
    if aa > bb:
        aa = bb
        return aa
    else:
        return aa, bb


ii = demo02(2, 9)
print(ii)

