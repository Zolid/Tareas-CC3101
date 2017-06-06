import p2b

list = 0.0
                #n          parteb   #m                  probtotal
def winGame(points, n, probWin, m, partidasac, prob):
    if points == n:
        return prob
    return winGame(points+1, n, probWin, m, partidasac+1, probWin*prob) + winGame(points - 1, n, probWin, m, partidasac + 1, prob * (1-probWin))


print winGame(0, 2, p2b.formula(10, 5, 3, [2, 0, 2, 10, 1, 20]), 4, 0, 1)
