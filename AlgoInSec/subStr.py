def L(ch, p):
    for i in range(len(p)-1, -1, -1):
        if(ch == p[i]):
            return i
    return -1

def BM(t, p):
    n = len(t)
    m = len(p)
    i = m - 1
    j = m - 1
    while(i <= n):
        if(p[j] == t[i]):
            if(j == 0):
                return i
            i -= 1
            j -= 1
        else:
            i = i + m - min(j, 1+L(t[i], p))
            j = m -1
    return -1

def brute(t, p):
    n = len(t)
    m = len(p)
    i, j  = 0, 0
    while(i+j < n):
        if(p[j] == t[i+j]):
            if(j == m-1):
                return i
            j += 1
        else:
            i += 1
            j = 0
    return -1

def pre(p, m):
	return [p[:i+1] for i in range(m)]
def suf(p, m):
	return [p[i:m] for i in range(m)]
def failureFunc(p):
	m = len(p)
	F = [0]*m
	F[0] = -1
	for j in range(1, m):
		pre_ = pre(p[:j], m)
		suf_ = suf(p[1:j], m)
		ar = list(set(pre_) & set(suf_))
		if(len(ar) == 0):
			F[j] = 0
		else:
			max_len = max([len(i) for i in ar])
			F[j] = max_len
	return F

def kmp(t, p):
	n = len(t)
	m = len(p)
	F = failureFunc(p)
	i = 0
	j = 0
	while(i+j < n):
		if(t[i+j] == p[j]):
			if(j == m-1):
				return i
			j += 1
		else:
			i = i + j - F[j]
			if(F[j] == -1):
				j = 0
			else:
				j = F[j]
	return -1

print(kmp('abacaabadcabacabaabb', 'abacab'))
# 10
print(kmp("this place it was brighter than tomorrow", 'it was'))
# 11
print(kmp("ABABDABACDABABCABAB", "ABCA"))
# 12
print(kmp("abcaab", "abd"))
# -1
print(kmp("an toan", "oan"))
# 4