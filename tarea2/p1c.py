def f(n):
    if n == 0:
        return 1
    return (5*f(n-1) + 2*g(n-1))%100

def g(n):
    if n == 0:
        return 2
    return (3*f(n-1) + g(n-1))%100

def sum(i):
    total = 0
    while i != -1:
        total += f(i) + g(i)
        i -= 1
    return total

k = 0
while k != 11:
    print str(f(k))+" "+str(g(k))+" "+str(k)
    k += 1