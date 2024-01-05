# -*- coding: utf-8 -*-


def use_math():
    import math

    return math.pi


def use_numpy():
    import numpy as np

    return np.pi


def use_radians():
    "math.radians() 将角度转换为弧度"
    import math

    return math.radians(180)


def use_acos():
    "使用反余弦函数"
    import math

    return 2 * math.acos(0)


if __name__ == '__main__':
    print(use_math())
    print(use_numpy())
    print(use_radians())
    print(use_acos())
