# -*- coding: utf-8 -*-

import p2b

probs = []


def winGame(points, n, probWin, m, turnGame, prob):
    if points == n:
        probs.append(prob)
    elif points + (m - turnGame) >= n:
        winGame(points + 1, n, probWin, m, turnGame + 1, probWin * prob)
        winGame(points - 1, n, probWin, m, turnGame + 1, prob * (1-probWin))

nym = raw_input("Entregue los enteros n y m (separados por espacios): ")
nym = nym.split(" ")
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

winGame(0, int(nym[0]), p2b.formula(int(first_line[0]), int(first_line[1]), int(first_line[2]), lista), int(nym[1]), 0, 1)

print "Resultado:"
print "%.3f" % sum(probs)