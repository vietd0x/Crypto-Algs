# a^k mod n
def Mod_Exp(a, k, n):
    b = 1
    if(k == 0):
        return b
    A = a
    if(k & 1):
        b = a
    lenk = len(str(bin(k))) - 2
    for i in range(lenk):
        A = A**2 % n
        k >>= 1
        if(k & 1 == 1):
            b = (A*b) % n
    return b

if __name__ == '__main__':
    # M ep kieu sang bytes
    M = bytes(input('Nhap plain text: '), 'utf-8')
    e = int(input('Nhap e: '))
    n = int(input('nhap n: '))
    # ep M sang int
    M = int(M.hex(), 16)
    print(f"C = {Mod_Exp(M, e, n)}")