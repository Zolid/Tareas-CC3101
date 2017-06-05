# -*- coding: utf-8 -*-
#Programación Pregunta 2 item b
#Las funciones estan de la forma solo para calcular Q_{n} desde A a B, si quisieramos de B a C o C a A
#habria que cambiar la forma de los pilotes de las funciones.

def Qn(n, A= "A", B ="B", C="C"):
  if (n == 1): #Caso base
      print "Mueva el disco " + str(n) + " '"+ A + "--->" + B+"'"
  else:
      Rn(n-1, A, C, B) #Movemos n-1 discos de A a C (dos pilotes)
      print "Mueva el disco " + str(n) + " '" + A + "--->" + B + "'" #mover el disco n de A a B.
      Rn(n-1, C, B, A); #Movemos n-1 discos de C a B (dos pilotes)

def Rn(n, A= "A", C="C", B="B"):
  if (n == 1): #Casos Bases
      print "Mueva el disco " + str(n) + " '" + A + "--->" + B + "'"
      print "Mueva el disco " + str(n) + " '" + B + "--->" + C + "'"
  else:
      Rn(n-1, A, B, C) #Movemos n-1 de A a C (dos pilotes)
      print "Mueva el disco " + str(n) + " '" + A + "--->" + B + "'" #Movemos el disco n de A a B
      Qn(n-1, C, A, B) #Movemos n-1 discos de C a A (un pilote)
      print "Mueva el disco " + str(n) + " '" + B + "--->" + C + "'" #Movemos el disco n de B a C
      Rn(n-1, A, C, B) #Movemos n-1 discos de A a C (dos pilotes)

Qn(3) #ejemplos de uso para un n=3 para mover n discos de A a B.