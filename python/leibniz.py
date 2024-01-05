# -*- coding: utf-8 -*-


def use_leibniz(rounds=10**6):
    """
    使用 莱布尼兹公式
    """
    k, s = 1, 0

    for i in range(rounds):
        if i % 2 == 0:
            s += 4/k
        else:
            s -= 4/k
        k += 2

    return s


if __name__ == '__main__':
    print(use_leibniz())
