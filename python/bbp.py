# -*- coding: utf-8 -*-

from mpmath import mp

def bbp_formula(digits):
    mp.dps = digits  # set number of decimal places
    pi = mp.mpf(0)
    for k in range(digits):
        pi += (mp.mpf(1)/(16**k))*((mp.mpf(4)/(8*k+1)) - (mp.mpf(2)/(8*k+4)) - (mp.mpf(1)/(8*k+5)) - (mp.mpf(1)/(8*k+6)))
    return pi

print(bbp_formula(100))
