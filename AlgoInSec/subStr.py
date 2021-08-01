# note TH subtring o cuoi text
def L(ch_T, P):
	n = len(P)
	for i in range(n-1, -2, -1):
		if(i == -1):
			return -1
		if(ch_T == P[i]):
			return i

def BM(T, P):
	m = len(P)
	n = len(T)
	i = m -1
	j = m -1
	while(i < n):
		if(P[j] == T[i]):
			if(j == 0):
				return i
			else:
				i -= 1
				j -= 1
		else:
			i = i + m - min(j, 1+L(T[i], P))
			j = m - 1
	return -1

def prefix(p):
	m = len(p)
	ar = [0]*m
	j=0 
	for i in range(1, m):
		while(j>=0 and p[j]!=p[i]):
			if j-1>=0:
				j=ar[j-1]
			else:
				j =- 1 
		j += 1
		ar[i] = j
	return ar

def lps(P):
	m = len(P)
	i = 0
	j = 1
	arr= [0] * m
	while j < m:
		if P[i] == P[j]:
			arr[j] = i + 1
			i+=1
			j+=1
		elif i == 0:
			arr[j] = 0
			j+=1
		else:
			i = arr[i - 1]
	return arr

print(prefix('abacab'))
# [0, 0, 1, 0, 1, 2]
def KMP(T, P):
	arr = lps(P)
	m = len(P)
	n = len(T)
	i = 0
	j = 0
	while (i < n):
		if (P[j] == T[i]):
			i += 1
			j += 1
		if(j == m):
			return i-j
		elif(i < n and P[j] != T[i]):
			if(j != 0):
				j = arr[j - 1]
			else:
				i+=1
	return -1

def search(T, P):
	m = len(P)
	n = len(T)
	i = 0
	j = 0
	while(i < n-m):
		if(P[j] == T[i+j]):
			if(j == m -1):
				return i
			j += 1
		else:
			j = 0
			i += 1
	return -1
# print(KMP('abacaabadcabacabaabb', 'abacab'))
# 10
# print(KMP("this place it was brighter than tomorrow", 'it was'))
# 11
# print(KMP("ABABDABACDABABCABAB", "ABCA"))
# 12