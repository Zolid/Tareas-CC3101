import math
import p2b

def combinatory(m, n):
    return math.factorial(m)/(math.factorial(n)*math.factorial(m-n))

def winGame(m, n, p):
    total = 0.0
    i = 1
    while i != m-n+1:
        total += combinatory(m-n+1, i)*math.pow(p, m-n+1-i)*math.pow(1.0 -p, i)
        i += 1
    return total

print winGame(5, 5, p2b.formula(20, 10, 2, [8, 3, 2, 50]))