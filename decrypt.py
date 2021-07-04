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
    blocksize = 1
    while(True):
        try:
            # ham n.to_bytes(blocksize, 'big') chuyen so nguyen sang dang bytes
            # nhung khi ta ko biet trc dc blocksize chinh xac la bao nhieu
            # neu nho hon thi se raise loi => dung try, except tang blocksize
            # den khi ko con loi => tinh dc msg 
            msg = Mod_Exp(C, d, n).to_bytes(blocksize, 'big')
            return msg
        except:
            blocksize += 1

if __name__ == '__main__':
    C = int(input('Nhap cipher text: '))
    d = int(input('Nhap d: '))
    n = int(input('nhap n: '))
    print(decrypt(C, d, n))
