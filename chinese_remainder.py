'''
n1, ... ,nk nguyen to cung nhau tung doi 1 thi he sau co NO DUY NHAT theo modulo n = n1...nk
x = a1 mod n1
x = a2 mod n2
  ...
x = ak mod nk
'''
import math

def inverse_Fp(a, p):
    u = a
    v = p
    x1, x2 = 1, 0
    while(u != 1):
        q = v // u
        r = v - q*u
        x = x2-q*x1

        v = u
        u = r
        x2 = x1
        x1 = x
    return x1%p

def chinese_remainder(n, a):
    sum = 0
    prod = math.prod(n)
    for a_i, n_i in zip(a, n):
        p = prod // n_i
        sum += a_i * p * inverse_Fp(p, n_i)
    return sum % prod

n = [9, 10, 23]#[11, 21, 26]
a = [7, 4, 15]#[10, 19, 20]
print(chinese_remainder(n, a))
