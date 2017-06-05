import math

f = [1]
g = [2]
total = 3
k = input("Ingrese un valor de k: ")
c = 1
while c <= k:
    print total
    f.append((5*f[c-1]+2*g[c-1])%100)
    g.append((3*f[c-1]+g[c-1])%100)
    total += f[c] + g[c]
    c += 1

print f
print g
print total%(math.pow(10, 9)+7)

