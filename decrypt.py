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

def decrypt(C, d, n):
    M = Mod_Exp(C, d, n)
    bPlainText = M.to_bytes((M.bit_length()+7) // 8, 'big')
    return bPlainText

if __name__ == '__main__':
    C = int(input('Nhap cipher text: '))
    d = int(input('Nhap d: '))
    n = int(input('nhap n: '))
    print(decrypt(C, d, n))
