# -*- coding: utf-8 -*-

#Pregunta 2 parte b

# Esta funcion calcula la probabilidad de ganar del jugador X
# con habilidad hx contra el jugador Y con habilidad hy.

def probabilidadGanarContra(hx, hy):
    return hx / (hx + hy)

#Esta funcion calcula la formula explicada en la parte a de la pregunta, es decir, la probabilidad de que el jugador X
#gane frente al resto de los jugadores.
#hx: habilidad del jugador X
#J: numero de jugadores sin contar el jugador X
#NG: Numero de grupos
#lista: lista con la informacion de los jugadores de cada grupo, los numeros pares (empezando del 0) de los indices de
# la lista corresponde a cada valor de G_{i}, y los indeces impares a las habilidades h_{i} de cada grupo.
def formula(hx, J, NG, lista):
    fhx = float(hx) #conversion de numero entero a numero flotante
    fJ = float(J) #conversion de numero entero a numero flotante #conversion de numero entero a numero flotante
    total = 0.0 #variable que almacena la suma acumulada de la sumatoria de la formula de la parte a
    cnt = 1 #contador para recorrer la lista
    while NG != 0: #mientras el NG distinto de 0
        total += probabilidadGanarContra(fhx, float(lista[cnt]))*float(lista[cnt-1]) #obtener la probailidad de ganar
        #de acuerdo a la habilidad de cada grupo
        NG -= 1 #contadores del loop
        cnt += 2 #recorrer las lista
    total = (1.0/fJ)*total #se mutiplica por probabilidad de elegir un jugador al azar
    return total #retorna la probabilidad de ganar frente al resto de los jugadores


if __name__ == '__main__':
    first_line = raw_input("Ingrese la primera linea como se describe en el enunciado, es decir hx, J, y el numero de grupos: ")
    first_line = first_line.split(" ")
    cnt = 0 #contador para almacenar la informacion de los grupos
    lista = []
    while cnt != int(first_line[2]):
        info = raw_input("Ingrese numero de jugadores del grupo G"+str(cnt+1)+" y la habilidad de los jugadores: " )
        info = info.split(" ")
        lista.append(int(info[0])) #se los valores a la que guardar la informacion de los grupos
        lista.append(int(info[1]))
        cnt += 1

    print "Resultado "+str(formula(int(first_line[0]), int(first_line[1]), int(first_line[2]), lista)) #se imprime el valor en pantalla

