from Leer import leerNum
import math
from scipy import stats
import matplotlib.pyplot as plt


# Generacion de la variable aleatoria con distribucion de Poisson
def gPoisson(lam: int, N: int = 0, T: float = 1, pse: list[float] = leerNum('data_Simulacion/Numeros.csv').copy()) -> int:
    Tp = T * pse.pop(0)
    if Tp >= math.exp(-lam):
        N += 1
        T = Tp
        return gPoisson(lam, N, T)
    else:
        return N


# Generacion de la variable aleatoria con distribucion Normal
def gNorm(mu: float, desv: float, pse: list[float] = leerNum('data_Simulacion/Numeros.csv').copy()) -> float:
    n: float = (sum([pse.pop(0) for i in range(12)]) - 6) * desv + mu
    if n <= 0:
        return gNorm(mu, desv)
    return n


# Funcion para generar un histograma dados los limites de los intervalos
def printHistogram(n: list[float] | list[int], bins: list[float] | list[int], title: str) -> None:
    plt.hist(x=n, bins=bins, color='#000000', rwidth=0.95)
    plt.title(title)
    plt.xticks(bins)
    plt.yticks(range(0, 21, 2))
    plt.show()


# Funcion para escribir la lista de numeros en un archivo csv
def writeNumbers(n: list[float] | list[int], name: str) -> None:
    with open(name + ".csv", 'w') as a:
        for num in n:
            a.write(f'{num}\n')


# Funcion para realizar la prueba de bondad de normalidad dada una lista de numeros, el valor de mu, desv estandar y el nivel de significancia
def testNormal(n: list[float], mu: float, desv: float, alpha: float = 0.05) -> bool:
    # Haciendo la prueba de de chi-cuadrada para una distribucion Normal
    numInt = int(math.sqrt(len(n)))
    anchoClase = (max(n)) / (numInt)
    li = 0.0
    ls = anchoClase
    intervals = []
    px = []
    for i in range(numInt):
        px.append(stats.norm.cdf(ls, mu, desv) - stats.norm.cdf(li, mu, desv))
        intervals.append([li, ls])
        li = ls
        ls += anchoClase
    px[0] = stats.norm.cdf(intervals[0][1], mu, desv)
    px[-1] = 1 - (sum(px) - px[-1])
    oi = [0 for i in intervals]
    for i in n:
        for x in intervals:
            if x[0] <= i < x[1]:
                oi[intervals.index(x)] += 1
                break
            elif i == x[1]:
                oi[intervals.index(x)] += 1
                break
    ei = [i * len(n) for i in px]
    errors = [((ei[i] - oi[i]) ** 2) / ei[i] for i in range(len(ei))]
    suma = sum(errors)
    chi2 = stats.chi2.ppf(1 - alpha, len(intervals) - 1)
    with open('data_GVarAl/Normal/Normal.csv', 'w') as f:
        f.write("Intervalo,oi,px,ei,errors\n")
        for i in range(len(intervals)):
            f.write(f"{round(intervals[i][0], 3)} - {round(intervals[i][1], 3)},{oi[i]},{px[i]},{ei[i]},{errors[i]}\n")
        f.write(f"\nTotales,{sum(oi)},{sum(px)},Chi calculada,{suma}")
        f.write(f"\n,,,Chi tablas,{chi2}")
    if (suma < chi2):
        print(f'La distribucion es normal -> {suma} < {chi2}')
        return True
    else:
        print('La distribucion no es normal')
        return False


# Funcion para realizar la prueba de bondad de Poisson, se requiere el valor de lamda y el nivel de significancia
def testPoisson(p: list[int], lam: float, alpha: float = 0.05) -> bool:
    nMin = min(p)
    nMax = max(p)
    if nMin != 0:
        intervals = [[0, nMin]]
        nMin += 1
    else:
        intervals = [[0, 1]]
        nMin += 2
    while nMin <= nMax:
        intervals.append([nMin, nMin + 1])
        nMin += 2
    oi = [0 for i in range(len(intervals) + 1)]
    for j in p:
        for i in intervals:
            if i[0] <= j <= i[1]:
                oi[intervals.index(i)] += 1
    px = []
    for i in intervals:
        px.append(sum([stats.poisson.pmf(x, lam) for x in range(i[0], i[1] + 1)]))
    px.append(1 - sum(px))
    if intervals[-1][1] == nMax:
        intervals.append([nMax + 1, nMin + 2])  # type: ignore
    else:
        intervals.append([nMin, nMin + 2])  # type: ignore
    ei = [i * len(p) for i in px]
    errors = [((ei[i] - oi[i]) ** 2 / ei[i]) for i in range(len(oi))]
    suma = sum(errors)
    chi2 = stats.chi2.ppf(1 - alpha, len(intervals) - 1)
    with open('data_GVarAl/Poisson/Poisson.csv', 'w') as f:
        f.write("Intervalo,oi,px,ei,errors\n")
        for i in range(len(intervals)):
            f.write(f"{intervals[i][0]}-{intervals[i][1]},{oi[i]},{px[i]},{ei[i]},{errors[i]}\n")
        f.write(f"\nTotales,{sum(oi)},{sum(px)},Chi calculada,{suma}")
        f.write(f"\n,,,Chi tablas,{chi2}")
    # print(intervals)
    if (suma < chi2):
        print(f'La distribucion es de Poisson -> {suma} < {chi2}')
        return True
    else:
        print('La distribucion no es de Poisson')
        return False

if __name__ == '__main__':
    # Probando con 50 numeros aleatorios generados con el algoritmo de Poisson
    lam = 17
    p = [gPoisson(lam) for i in range(50)]
    writeNumbers(p, 'data_GVarAl/Poisson/gPoisson')
    testPoisson(p, lam)

    # Probando con 100 numeros aleatorios generados con el algoritmo normal
    mu = 10.0
    desv = 6.5
    n = [gNorm(mu, desv) for i in range(100)]
    writeNumbers(n, 'data_GVarAl/Normal/gNormal')
    testNormal(n, mu, desv)
