# -*- coding: utf-8 -*-

#Pregunta 1 parte d

#librerias a utilizar
import math
import time

start_time = time.time()
f = [1] #lista para almacenar los valores de las recursiones de la funcion f
g = [2] #lista para almacenar los valores de las recursiones de la funcion g
total = 3 #variable que ira sumando de forma acumulada los valores de la funciones
# f y g para cada iteracion i
a = input("Ingrese un valor de a: ") #variable que almacena el valor del ponderador a para f
b = input("Ingrese un valor de b: ") #variable que almacena el valor del ponderador b para g
m = input("Ingrese un valor de m: ") #variable que almacena el valor del modulo m para f
c = input("Ingrese un valor de c: ") #variable que almacena el valor del ponderador c para f
d = input("Ingrese un valor de d: ") #variable que almacena el valor del ponderador d para g
l = input("Ingrese un valor de l: ") #variable que almacena el valor del modulo l para g
k = input("Ingrese un valor de k: ") #variable que almacena el valor k hasta donde se quiere calcular en
# en la sumatoria
i = 1 #variable de contador para las i iteraciones o la para la sumatoria pedidad en la pregunta
while i <= k: #loop para caculatar todos las variables de la sumatoria
    f.append((a*f[i-1]+b*g[i-1])%m) #Esto almacena los valores de la funcion f(n) en la lista f
    g.append((c*f[i-1]+d*g[i-1])%l) #Esto almacena los valores de la funcion g(n) en la lista g
    total += f[i] + g[i] #suma alcumulada
    i += 1 #aumento del contador

print total%(math.pow(10, 9)+7) #impresion de valor en pantalla aplicando el modulo sugerido
print("--- minutos --- " + str((time.time() - start_time)/60.0)) #para calcular el tiempo del algoritmo