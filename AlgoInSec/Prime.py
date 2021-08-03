import math
import random

def ModExp(a, k, n):
	res = 1
	if(k == 0):
		return 1
	if(k&1):
		res = a
	while(k > 0):
		a = a**2 %n
		k >>= 1
		if(k&1):
			res = res*a %n
	return res

def simpleSieve(n):
    mark = [True]*(n+1)
    for p in range(2, n+1):
        if(mark[p]):
            for i in range(p*p, n+1, p):
                mark[i] = False
        else:
            continue
    return [p for p in range(2, n+1) if(mark[p])]

def SegmentSieve(n, m):
    prime = simpleSieve(m+1)
    l = m+2
    r = m*2 + 1
    while(l <= n):
        if(r > n):
            r = n
        mark = [True]*m
        for p in range(len(prime)):
            if(prime[p]**2 > r):
                continue
            lseg = (l // prime[p])*prime[p]
            if(lseg < l):
                lseg += prime[p]
            
            for i in range(lseg, r+1, prime[p]):
                mark[i-l] = False

        for i in range(l, r+1):
            if(mark[i-l]):
                prime.append(i)
        l += m
        r += m
    return prime

# print(SegmentSieve(100, 2))


# # tim thua so ko tam thuong
# # x^2 + c (c # 0, 2)
def PolardRho(n, c = 1):
    a = 2
    b = 2
    while(True):
        a = (a**2 + c) % n
        b = (b**2 + c) % n
        b = (b**2 + c) % n
        d = GCD(abs(a-b), n)
        if(1 < d and d < n):
            return d
        if(d == n):
            return -1

# test :: list
def fermat(n, iter, test):
    p = 0
    for i in range(iter):
        if(pow(int(test[i]), n-1) % n != 1):
            print(f'Co so a={test[i]}: Hop so')
        else:
            p += 1
    if(p == iter):
        return 'co the la nguyen to'
    return 'la hop so'



# ptich thanh thua so ngto
def update_dict(n, dict_):
    if(n in dict_.keys()):
        dict_[n] += 1
    else:
        dict_.update({n:1})
    return dict_

n = int(input())
print(f"n = {n} = ", end = '')
dict_ = {}
r = n
while(r % 2 == 0):
    update_dict(2, dict_)
    r //= 2
for i in range(3, math.ceil(math.sqrt(n)), 2):
    while(r%i == 0):
        update_dict(i, dict_)
        r //= i
if(r > 2):
    update_dict(r, dict_)

for i, k in enumerate(dict_.keys()):
    if(i == len(dict_)-1):
        print(f"{k}^{dict_[k]}")
    else:
        print(f"{k}^{dict_[k]} + ", end = '')

def miller_rabin(n, t = 20):
    # n-1 = 2^s * r
    s = 0
    r = n -1
    while(r & 1 == 0):
        r >>= 1
        s += 1
    # đã tính được r và s
    for i in range(t):
        a = random.randint(2, n-2)

        y = Mod_Exp(a, r, n)
        if(y != 1 and y != n-1):
            j = 1
            while(j <= s-1 and y != n-1):
                y = y**2 % n
                if(y == 1):
                    return False
                j += 1
            if(y != n-1):
                return False
    return True

# ans = PolardRho(43567127)
# print(ans)

# print(fermat(561,1))

# print(Mod_Exp(5, 596, 1234))
# print(pow(5, 596, 1234))
# print(Mod_Exp(25, 705, 3542))
# print(miller_rabin(30, 2))

# print(gcd(28150488, 28150488))
# print(SegmentSieve(n =30, delta = 1))

# print(fermat(91, 1))
# print(miller_rabin(91, 1, [2]))
