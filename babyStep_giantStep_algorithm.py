# https://www.geeksforgeeks.org/discrete-logarithm-find-integer-k-ak-congruent-modulo-b/
'''
Tinh log_a(b) tren Z*n vs a la ptu sinh cua Z*n
nhom nhan cua Zn la Z*n = {a thuoc Zn | GCD(a, n) = 1}
'''
import math;
 
def discreteLogarithm(a, b, m):
    n = int(math.sqrt(m) + 1);
    value = [0] * m;
    for i in range(n, 0, -1):
        value[pow(a, i * n, m)] = i;
    for j in range(n):
        cur = (pow(a, j, m) * b) % m;
        if (value[cur]):
            ans = value[cur] * n - j; 
            if (ans < m):
                return ans;
    return -1;

a = 31;
b = 45;
m = 61;
print(discreteLogarithm(a, b, m));
