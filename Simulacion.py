from Pseudo import Pseudo
import math


# Parametros iniciales para generar los numeros pseudo-aleatorios
x0 = 6
g = 13
k = 15
c = 8191
alfa = 0.05
# Se generan los pseudo y se les aplican cada una de las pruebas correspondientes
print("")
n = Pseudo(x0, g, k, c)
n.gLineal()
n.pMedias(alfa)
n.pVarianza(alfa)
n.pUniformidad(alfa)
n.pIndependencia(alfa)
print("")
