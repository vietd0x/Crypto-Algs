'''
return 0  -> n|a
return 1  -> a thuoc Qn  - a la thang du b2 theo modulo n
return -1 -> a thuoc ~Qn - a la bat thang du b2 theo modulo n
'''
def jacobi_symbol(a, n):
    assert(n > a > 0 and n%2 == 1)
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0
