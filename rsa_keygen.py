import random

def Mod_Exp(a, k, n):
    b = 1
    if(k == 0):
      return b
    A = a
    if(k & 1):
      b = a
    lenk = len(str(bin(k))) - 2 # '0b'
    for i in range(lenk):
      A = A**2 % n
      k >>= 1
      if(k & 1 == 1):
          b = (A*b) % n
    return b

def check_composite(n, a, r, s):
    x = Mod_Exp(a, r, n)
    if(x == 1 or x== n-1):
        return False
    for r in range(s):
        x = x*x%n
        if(x == n-1):
            return False
    return True

def miller_rabin(n, iter_ = 20):
    # n-1 = 2^s * r
    s = 0
    r = n -1
    while(r & 1 == 0):
        r >>= 1
        s += 1 
    for i in range(iter_):
        a = random.randint(2, n-2)
        if(check_composite(n, a, r, s)):
            return False
    return True

def selectNum():
    while(True):
        n = random.getrandbits(128)
        if not (n & 1):
            continue
        if(miller_rabin(n)):
            return n

def ExtEuclidean(a, b):
    if(b == 0):
        return a, 1, 0
    if(a < b):
        tmp = a
        a = b
        b = tmp
    x1, x2, y1, y2 = 0, 1, 1, 0
    while(b > 0):
        q = a//b
        r = a- q*b
        x = x2-q*x1
        y = y2-q*y1

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return a, x2, y2

def GCD(a, b):
    if(a == 0):
        return b
    return GCD(b%a, a)

def key_gen():
    p = selectNum()
    q = selectNum()
    # test prime num here: https://www.wolframalpha.com/input/?i=Is+10001+prime%3F&lk=3
    n = p*q
    print(f'p = {p}\nq = {q}')
    phi_n = (p-1)*(q-1)
    while(True):
        # 1 < e < phi_n
        e = random.randint(2, phi_n-1)
        if(GCD(e, phi_n)):
            gcd, s, t = ExtEuclidean(phi_n, e)
            if(gcd == (s * phi_n + t * e)):
                d = t % phi_n
                return e, n, d
if __name__ == '__main__': 
   e, n, d = key_gen()
   print(f"e = {e}\nn = {n}\nd = {d}")