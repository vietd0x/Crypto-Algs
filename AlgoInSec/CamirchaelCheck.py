import random
def GCD(a, b):
    if(a == 0):
        return b
    return GCD(b%a, a)

def miller_rabin(n):
    # n-1 = 2^s.r
    r = n-1
    s = 0
    while(r&1 == 0):
        r >>= 1
        s += 1
    for i in range(10):
        a = random.randint(2, n-2)
        y = pow(a, r, n)
        if(y != 1 and y != n-1):
            j = 1
            while(j <= s-1 and y != n-1):
                y = y*y %n
                if(y == 1):
                    return False
                j += 1
            if(y != n-1):
                return False
    return True
def isCamichael(n):
    if(n < 561):
        return False
    if(miller_rabin(n)):
        return False
    for i in range(2, n, 1):
        if(GCD(i, n) == 1):
            if(pow(i, n-1, n) != 1):
                return False
    return True