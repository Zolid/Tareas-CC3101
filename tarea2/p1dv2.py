import math
import time

start_time = time.time()
f = [1]
g = [2]
total = 3
a = input("Ingrese un valor de a: ")
b = input("Ingrese un valor de b: ")
m = input("Ingrese un valor de m: ")
c = input("Ingrese un valor de c: ")
d = input("Ingrese un valor de d: ")
l = input("Ingrese un valor de l: ")
k = input("Ingrese un valor de k: ")
count = 1
while count <= k:
    f.append((a*f[count-1]+b*g[count-1])%m)
    g.append((c*f[count-1]+d*g[count-1])%l)
    total += f[count] + g[count]
    count += 1

print total%(math.pow(10, 9)+7)
print("--- minutes --- " + str((time.time() - start_time)/60.0))