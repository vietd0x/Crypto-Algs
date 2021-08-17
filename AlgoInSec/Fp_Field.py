import math

def Fp2matrix(a, p, w):
    t = math.ceil(math.ceil(math.log(p, 2))/ w)
    A = [0]*t
    for i in range(t-1, -1, -1):
        tmp = 2**(w*i)
        A[t-1-i] = a // tmp
        a -= A[t-1-i]*tmp

def sumOf2LargeNum(a, b, p, w):
    t = math.ceil(math.ceil(math.log(p, 2))/ w)
    a = Fp2matrix(a, p, w, t)
    b = Fp2matrix(b, p, w, t)
    c = [0, [0]*t]
    n = 2 **w
    for i in range(t-1, -1, -1):
        sum = a[i] + b[i] + c[0]
        if(sum >= n):
            c[0] = 1
        else:
            c[0] = 0
        c[1][i] = sum %n
    return c

def diff2LargeNum(a, b, p, w):
    t = math.ceil(math.ceil(math.log(p, 2))/w)
    a = Fp2matrix(a, p, w, t)
    b = Fp2matrix(b, p, w, t)
    c = [0, [0]*t]
    n = 2**w
    for i in range(t-1, -1, -1):
        diff = a[i] - b[i] - c[0]
        if(diff < 0):
            c[0] = 1
        else:
            c[0] = 0
        c[1][i] = diff%n
    return c

def isGreaterOrEqual(a, b):
	for i in range(len(a)):
		if(a[i] < b[i]):
			return False
		if(a[i] > b[i]):
			return True
	return True

def add_in_Fp(a, b, p, w):
	if(type(a) is not list and type(b) is not list):
		a = Fp2matrix(a, p, w)
		b = Fp2matrix(b, p, w)
		
	c = sumOf2LargeNum(a, b, p, w)
	ar_p = Fp2matrix(p, p, w, t)
    if(c[0] == 1):
        return DiffOf2LargeNum(c[1], ar_p, p, w, t)[1]
    else:
        if(GreaterOrEqu(c[1], ar_p)):
            return DiffOf2LargeNum(c[1], ar_p, p, w, t)[1]
        else:
            return c[1]

def sub_in_Fp(a, b, p, w):
	if(type(a) is not list and type(b) is not list):
		a = Fp2matrix(a, p, w)
		b = Fp2matrix(b, p, w)

	t = math.ceil(math.ceil(math.log(p, 2))/w)
	c = diffOf2LargeNum(a, b, p, w)
	if(c[0] == 1):
		arr_d = Fp2matrix(p, p, w)
		ans = sumOf2LargeNum(arr_d, c[1], p, w)[1]
		return ans
	else:
		return c

def mulInFp(a, b, p, w):
    t = len(a)
    c = [0]* (t*2)
    n = 2**w
    for i in range(t-1, -1, -1):
        carry = 0
        for j in range(t-1, -1, -1):
            tmp = a[i] * b[j] + c[i+j+1]+ carry
            c[i+j+1] = tmp % n
            carry = (tmp >> w) % n
        c[i] = carry
    return c

# a >= b
def ExtEuclidean(a, b):
	if(b == 0):
		return a, 1, 0
	if(a < b):
		tmp = a
		a = b
		b = tmp
	x1 = 0
	x2 = 1
	y1 = 1
	y2 = 0
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
# return the val * a mod p = 1
def inverse_Fp(a, p):
	u = a
	v = p
	x1, x2 = 1, 0
	while(u != 1):
		q = v // u
		r = v - q*u
		x = x2-q*x1

		v = u
		u = r
		x2 = x1
		x1 = x
	return x1%p


#___________________________________TestCases_______________________________________
# print(add_in_Fp(a=[157,0,173,23], b=[169,1,0,64], w=8, p=2147483646))
# print(add_in_Fp(a=38762497, b= 568424364, w=8, p=2147483647))
# print(mulInFp(a = [0, 11, 173, 248] ,b = [0, 1, 226, 64],w = 8,p = 2147483647))
# [0, 0, 0, 22, 0, 120, 110, 0]
# print(ExtEuclidean(a= 489573857, b= 5))
# print(EEA(489573857, 5))
# print(inverse_Fp(20200275038338720, 18872986474482592,))
# print(inverse_Fp(45682375, 489573857))
# print(mulInFp([0, 8, 1, 103], [0, 0, 127, 37], 2147483647, 8))
# [0, 0, 0, 3, 249, 218, 76, 227]
