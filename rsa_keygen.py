import random

# tính a^k mod n
# thuật toán nhân bình phương có lặp trong slide
def Mod_Exp(a, k, n):
    res = 1
    if(k == 0):
        return ans
    if(k&1):
        res = a
    while(k > 0):
        a = a**2  % n
        k >>= 1
        if(k&1):    
            res = (a*res) % n
    return res

# thuật toán ktra số nguyên tố Miller Rabin
def miller_rabin(n, iter_ = 20):
    # n-1 = 2^s * r
    s = 0
    r = n -1
    # r chia hết cho 2
    while(r & 1 == 0):
        r >>= 1 # chia r cho 2
        s += 1  # tăng s
    # đã tính được r và s
    for i in range(iter_):
        # 2 <= a <= n-2 như trong slide
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

# hàm này trả về random 1 số nguyên tố
def selectNum():
    while(True):
        # lấy random 1 số 2048 bit
        n = random.getrandbits(2048)
        # n là chẵn thì cho chạy tiếp để lấy giá trị n khác
        if not (n & 1):
            continue
        # ktra xem có là nguyên tố ko?
        if(miller_rabin(n)):
            return n
# thuật toán euclid mở rộng trong silde
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

def key_gen():
    p = selectNum()
    q = selectNum()
    n = p*q
    #print(f'p = {p}\nq = {q}')
    phi_n = (p-1)*(q-1)
    
    while(True):
        # 1 < e < phi_n
        e = random.randint(2, phi_n-1)
        # phi_n*x + e*y = gcd
        # tim e until gcd TM = 1, hay GCD(phi_n, e) = 1
        # <=> e^-1 mod phi_n = y
        gcd, x, y = ExtEuclidean(phi_n, e)
        if(gcd == 1):
            # d = inverse(e) % phi_n
            d = y % phi_n
            return e, n, d

if __name__ == '__main__': 
   e, n, d = key_gen()
   print(f"e = {e}\nn = {n}\nd = {d}")
