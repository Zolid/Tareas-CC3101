import math


f = [1]
g = [2]

count = 1

a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
c = input("Ingrese el valor de c: ")
d = input("Ingrese el valor de d: ")
m = input("Ingrese el valor de m: ")
l = input("Ingrese el valor de l: ")

loop2 = l-1
loop1 = m-1
k = input("Ingrese valor de k ")
total = 3
while count <= k:
    print total, count
    f.append((a * f[count - 1] + b * g[count - 1]) % m)
    g.append((c* f[count - 1] + d*g[count - 1]) % l)
    #print (a * f[count - 1] + b * g[count - 1]) % m, (c* f[count - 1] + d*g[count - 1]) % l
    total += (f[count] + f[count])
    count += 1

print f
print g
print total%(math.pow(10, 9) + 7)

