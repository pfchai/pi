# -*- coding: utf-8 -*-

from mpmath import mp

# Set the decimal precision
mp.dps = 101  # 100 digits of precision + 1 for safety

def ramanujan_sato_series(iterations):
    pi = mp.mpf(0)  # mpf is a floating point number with arbitrary precision
    for k in range(iterations):
        pi += (mp.factorial(4*k)*(1103+26390*k))/((mp.factorial(k)**4)*(396**(4*k)))
    pi *= (2*mp.sqrt(2))/9801
    return 1/pi

print(ramanujan_sato_series(50))
