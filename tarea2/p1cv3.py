import math

f = [1]
g = [2]
total = [3]
loop = 99
c = 1
while c <= loop:
    f.append((5 * f[c - 1] + 2 * g[c - 1]) % 100)
    g.append((3 * f[c - 1] + g[c - 1]) % 100)
    total.append(f[c] + g[c])
    c += 1


value = sum(total)

k = input("Ingrese valor de k: ")

totalValue = ((k / 100)*value + sum(total[0:(k%100)+1]))%(math.pow(10, 9)+7)

print totalValue