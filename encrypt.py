# a^k mod n
def Mod_Exp(a, k, n):
    ans = 1
    if(k == 0):
        return ans
    if(k&1):
        ans = a
    lenk = len(str(bin(k))) - 2
    for i in range(lenk):
        a = a**2  % n
        k >>= 1
        if(k&1):    
            ans = (a*ans) % n
    return ans

if __name__ == '__main__':
    # M ep kieu sang bytes
    M = bytes(input('Nhap plain text: '), 'utf-8')
    e = int(input('Nhap e: '))
    n = int(input('nhap n: '))
    # ep M sang int
    M = int(M.hex(), 16)
    print(f"C = {Mod_Exp(M, e, n)}")
