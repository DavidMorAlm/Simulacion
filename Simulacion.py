from Pseudo import Pseudo
import math


x0 = 6
g = 13
k = 15
c = 8191
alfa = 0.05

print("")
n = Pseudo(x0, g, k, c)
n.gLineal()
n.pMedias(alfa)
n.pVarianza(alfa)
n.pUniformidad(alfa)
n.pIndependencia(alfa)
print("")
