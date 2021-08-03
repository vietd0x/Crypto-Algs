import random

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

def gcd(a, b):
	if(a == 0):
		return b
	return gcd(b%a, a)

def PolardRho(n, c=-1):
	if(not n&1):
		return 2
	x, y = 2, 2
	while(True):
		x = (x**2 + c) % n
		y = (y**2 + c) % n
		y = (y**2 + c) % n
		d = gcd(abs(x - y), n)
		if(1 < d and d < n):
			if(miller_rabin(d)):
				return d
		if(d == n):
			c += 2
			return PolardRho(n, c)

def miller_rabin(n):
	if(n < 4):
		return (n == 2) | (n == 3)
	r = n-1
	s = 0
	while(r&1 == 0):
		r >>= 1
		s += 1
	for i in range(10):
		a = random.randint(2, n-2)
		y = pow(a, r, n)
		if(y != 1 and y != n-1):
			j = 1
			while(j <= s-1 and y != n-1):
				y = y **2 %n
				if(y == 1):
					return False
				j += 1
			if(y != n -1):
				return False
	return True

def update_dict(n, _dict):
	if(n in _dict.keys()):
		_dict[n] += 1
	else:
		_dict.update({n:1})
	return _dict

def primeFact(n):
	prime_factor_dict = {} 
	if n < 2:
		return n
	s = 0
	while(n&1 == 0):
		n >>= 1
		s += 1
	if(s > 0):
		prime_factor_dict.update({2:s})
	while(n > 1):
		if(miller_rabin(n)):
			update_dict(n, prime_factor_dict)
			return prime_factor_dict
		v = PolardRho(n)
		update_dict(v, prime_factor_dict)
		n //= v
	return prime_factor_dict

if __name__ == '__main__':
	for i in range(101):
		print(f'{i} = {primeFact(i)}')
	