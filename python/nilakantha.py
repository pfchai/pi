# -*- coding: utf-8 -*-

def use_nilakantha(rounds=10**6):
    s = 3

    for i in range(1, rounds):
        k = 2 * i
        if i % 2 == 1:
            s += 4 / (k * (k+1) * (k+2))
        else:
            s -= 4 / (k * (k+1) * (k+2))

    return s


if __name__ == '__main__':
    print(use_nilakantha())
