# -*- coding: utf-8 -*-

#Pregunta 1 parte c

import math

f = [1] #lista para almacenar los valores de las recursiones de la funcion f
g = [2] #lista para almacenar los valores de las recursiones de la funcion g
total = [3] #lista para almacenar los valores de las recursiones se la sumatoria f(i) + g(i) para
# todo i hasta n
loop = 99 #limite para calcular los valores del periodo en cada funcion
i = 1 #contador para calcular los valores del periodo de ambas funciones
while i <= loop:
    f.append((5 * f[i - 1] + 2 * g[i - 1]) % 100) #Se almacenan todos los valores de la recursiones en la lista f
    g.append((3 * f[i - 1] + g[i - 1]) % 100) #Se almacenan todos los valores de la recursiones en la lista g
    total.append(f[i] + g[i]) #Se almacenan todos los valores de la recursiones para cada uno de los i valores en la
    #sumatoria
    i += 1 #se aumenta el contador


value = sum(total) #Se calcula la suma de todos los elementos de la sumatoria dentro de lista total
try:
    k = input("Ingrese valor de k: ") #ingreso del valor k a calcular

    totalValue = ((k / 100)*value + sum(total[0:(k%100)+1]))%(math.pow(10, 9)+7) #formula explica en la parte p1b,
    #para calcular el valor de la sumatoria eficientemente dado un k

    print totalValue #impresion en pantalla del valor obtenido dado el k

#errores de ejecucion
except SyntaxError:
    print "Debe agregar solo números"

except NameError:
    print "Debe agregar solo números"

except TypeError:
    print "Debe agregar solo numeros"