# -*- coding: utf-8 -*-

#Pregunta 1 parte e

#liberia a utilizar
import math
import time

start_time = time.time()

f = [1] #lista para almacenar los valores de las recursiones de la funcion f
g = [2] #lista para almacenar los valores de las recursiones de la funcion g

dicc = {} #el diccionario sirve para determinar si las tuplas para determinar cuando se inicia un nuevo ciclo
#en los valores de f y g


a = input("Ingrese un valor de a: ") #variable que almacena el valor del ponderador a para f
b = input("Ingrese un valor de b: ") #variable que almacena el valor del ponderador b para g
m = input("Ingrese un valor de m: ") #variable que almacena el valor del modulo m para f
c = input("Ingrese un valor de c: ") #variable que almacena el valor del ponderador c para f
d = input("Ingrese un valor de d: ") #variable que almacena el valor del ponderador d para g
l = input("Ingrese un valor de l: ") #variable que almacena el valor del modulo l para g
k = input("Ingrese un valor de k: ") #variable que almacena el valor k hasta donde se quiere calcular

i = 1 #contador i
dicc[(f[0], g[0])] = 0 #agregamos los valores al diccionario, donde las llaves son una tupla de los valores
# de f y g, y el valor el indice que determina los valores de f y g
n0 = 0 #para almacenar el indice cuando empieza un ciclo
n1 = 0 #para almacenar el indice cuando termina un ciclo
while True:
    f.append((a * f[i - 1] + b * g[i - 1]) % m)  # Esto almacena los valores de la funcion f(n) en la lista f
    g.append((c * f[i - 1] + d * g[i - 1]) % l)  # Esto almacena los valores de la funcion g(n) en la lista g
    if dicc.has_key((f[i], g[i])): #si la tupla de los valores de f y g estan en el diccionario se almacenan los valores
        #en n0 y n1, y se cortar el loop
        n0 = dicc.get((f[i], g[i]))
        n1 = i
        break
    else:
        dicc[(f[i], g[i])] = i #se almacenan los i indices en el diccionario
        i += 1  # aumento contador

notloop = sum(f[0:n0]) + sum(g[0:n0]) #se calcula la sumatoria de valores que no estan en un periodo
L = sum(f[n0:n1]) + sum(g[n0:n1]) #el valor que existe en un periodo
numCompLoop = (k+1-n0)/(n1 - n0) #calculamos el numero de periodos completos existentes
loopIncomplete = sum(f[n0:(k+1-n0)%(n1-n0)]) + sum(g[n0:(k+1-n0)%(n1-n0)]) #sumatoria de un periodo no completo

print (notloop + numCompLoop*L + loopIncomplete)%(math.pow(10, 9)+7) #imprime en pantalla el valor con el modulo
#sugerido en el enunciado.

print "Tiempo en segundos es: "+str(time.time() - start_time)