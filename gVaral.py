from Leer import leerNum
import math

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
    x = 0.0
    for i in range(12):
        x += l.pop(0)
    return (x-6)*desv + mu

print([gPoisson(10) for i in range(10)])