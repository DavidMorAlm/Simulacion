from Leer import leerNum
import math
from scipy import stats
import matplotlib.pyplot as plt

l = leerNum('Numeros.csv')


# Generacion de la variable aleatoria con distribucion de Poisson
def gPoisson(lam: int, N: int = 0, T: float = 1) -> int:
    Tp = T * l.pop(0)
    if Tp >= math.exp(-lam):
        N += 1
        T = Tp
        return gPoisson(lam, N, T)
    else:
        return N


# Generacion de la variable aleatoria con distribucion Normal
def gNorm(mu: float, desv: float) -> float:
    n: float = (sum([l.pop(0) for i in range(12)]) - 6) * desv + mu
    if n <= 0:
        return gNorm(mu, desv)
    return n


# Funcion para generar un histograma dados los limites de los intervalos
def printHistogram(bins: list[float], title: str) -> None:
    plt.hist(x=n, bins=bins, color='#000000', rwidth=0.95)
    plt.title(title)
    plt.xticks(bins)
    plt.yticks(range(0, 21, 2))
    plt.show()


mu: float = 10
desv: float = 6.5

# Generando la variable aleatoria con distribucion Normal
n = [gNorm(mu, desv) for i in range(100)]

# Haciendo la prueba de de chi-cuadrada para una distribucion Normal
numInt = int(math.sqrt(len(n)))
anchoClase = (max(n)) / (numInt )
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
if (sum(errors) < stats.chi2.ppf(0.95, len(intervals) - 1)):
    print('La distribucion es normal')
else:
    print('La distribucion no es normal')
