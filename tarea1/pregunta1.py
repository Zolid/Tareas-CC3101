# -*- coding: utf-8 -*-
#Pregunta 1d de la tarea 1.

#Dado un valor de d de billetes obtenemos cuantas secuencias de billetes (de 3 o 5) puede formar ese valor d.
def secuencias(d):
    if (d == 0): #casos bases para cortar la recursion
        return 0
    if (d == 1):
        return 0
    if (d == 2):
        return 0
    if (d == 3):
        return 1
    if (d == 4):
        return 0
    if (d == 5):
        return 1
    return secuencias(d - 3) + secuencias(d - 5) #definición inductiva que se cumple para d, mayores a 5.

print secuencias(25) #ejemplo de uso para un d = 25.