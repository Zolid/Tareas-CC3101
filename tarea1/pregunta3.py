# -*- coding: utf-8 -*-
#Pregunta 3b de la tarea 1.

import random #liberia random

#Dada una lista elegimos un elemento aleatorio, cuando a priori no conocemos el largo de la lista.
def aleatorio(list):
    c = 0 #contador para recorrer las lista
    num = list[0] #guardamos el primer elemento
    i = 1.0 #contador de probabilidad de medida que se recorren los elementos de la lista
    while True: #loop infinito, debido a que a priori no conocemos el largo de lista
        try:
            rand = random.random() #valor aleatorio que "elige" si elemento sera reemplazado o no
            prob = float((1.0 / (i+1.0))) #calculamos la probabilidad respectiva
            if prob < rand: #Si el valor aleatorio es mayor a la probalilidad el elemento se mantiene.
                i += 1.0
                c += 1
            else:
                num = list[c] #Sino, es reemplazado.
                i += 1.0
                c += 1
        except IndexError: #Como a priori no conocemos el largo de la lista usamos un try-except, para
            break         #cortar el loop, si se detecta un indice fuera de largo de la lista se corta el loop.
    print '"'+str(num)+'"' #retornamos elemento.

aleatorio([1,3,5,2,1,9]) #ejemplo del enunciado.