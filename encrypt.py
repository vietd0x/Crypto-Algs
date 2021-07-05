# a^k mod n
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

if __name__ == '__main__':
    # plaintext ep kieu sang bytes
    bPlaintext = bytes(input('Nhap plain text: '), 'utf-8')
    e = int(input('Nhap e: '))
    n = int(input('nhap n: '))
    # ep bPlaintext sang int
    M = int(bPlaintext.hex(), 16)
    print(f"C = {Mod_Exp(M, e, n)}")
