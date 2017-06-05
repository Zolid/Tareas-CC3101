
# Esta funcion calcula la probabilidad de ganar del jugador
# con habilidad hx contra el jugador con habilidad hy.

def probabilidadGanarContra(hx, hy):
    return hx / (hx + hy)


def formula(hx, J, NG, lista):
    fhx = float(hx)
    fJ = float(J)
    fNG = float(NG)
    total = 0.0
    cnt = 1
    while NG != 0:
        total += probabilidadGanarContra(hx, float(lista[cnt]))*float(lista[cnt-1])
        NG -= 1
        cnt += 2
    total = (1.0/fNG)*total
    return total



hx = input("Ingrese hx: ")
J = input("Ingrese el numero de jugadores: ")
NG = input("Ingrese el numero de grupos G: ")
cnt = 0
lista = []
while cnt != NG:
    info1 = input("Ingrese numero de jugadores del grupo G"+str(cnt+1)+": ")
    info2 = input("Ingrese la habilidad de los jugadores grupo G"+str(cnt+1)+": ")
    lista.append(info1)
    lista.append(info2)
    cnt += 1

print "Resultado "+str(formula(hx, J, NG, lista))

