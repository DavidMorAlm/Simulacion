import math
from scipy import stats as st


class Pseudo:

    def __init__(self, x0: int, g: int, k: int, c: int):
        self.x0 = x0
        self.g = g
        self.k = k
        self.c = c
        self.m = int(math.pow(2, self.g))
        self.a = 1 + (4 * self.k)
        self.l = []
        self.archivo = open("data_Simulacion/Numeros.csv", "w")

    def gLineal(self):
        for i in range(self.m):
            ri = self.x0 / (self.m - 1)
            self.x0 = ((self.a * self.x0) + self.c) % self.m
            self.l.append(ri)
            with open("data_Simulacion/Numeros.csv", "a") as self.archivo:
                self.archivo.write(str(ri) + "\n")

    def pMedias(self, alpha : float) -> bool:
        result = False
        p = 0
        z = abs(st.norm.ppf(alpha / 2))
        li = (1 / 2) - (z * (1 / math.sqrt(12.0 * self.m)))
        ls = (1 / 2) + (z * (1 / math.sqrt(12.0 * self.m)))
        for i in self.l:
            p += i
        p /= self.m
        if li <= p <= ls:
            print(
                f"No se puede rechazar que el conjunto ri tiene un valor esperado de 1/2 con un nivel de aceptacion de {(1 - alpha) * 100:.0f}%")
            result = True
        else:
            print("Se rechaza que el conjunto ri tiene un valor esperado de 1/2.")
            result = False
        return result

    def pVarianza(self, alpha: float) -> bool:
        result = False
        gl = self.m - 1
        p = 0
        var = 0
        for i in self.l:
            p += i
        p /= self.m
        for i in self.l:
            var += math.pow((i - p), 2)
        var /= gl
        ls = st.chi2.isf(alpha / 2, gl) / (12 * gl)
        li = st.chi2.isf(1 - alpha / 2, gl) / (12 * gl)
        if li <= var <= ls:
            print(
                f"No se puede rechazar que el conjunto ri tiene una varianza de 1/12 con un nivel de aceptacion de {(1 - alpha) * 100:.0f}%")
            result = True
        else:
            print("Se rechaza que el conjunto ri tiene una varianza de 1/12.")
            result = False
        return result

    def pUniformidad(self, alpha: float) -> bool:
        result = False
        m = int(math.sqrt(self.m)) + 1
        gl = m - 1
        chi = st.chi2.isf(alpha, gl)
        anchoClase = 1 / m
        estChi = 0
        freqEsperada = int(self.m / m + 1)
        intervalos = [[], [], []]
        for i in range(m):
            intervalos[0].append(i * anchoClase)
            intervalos[1].append((i + 1) * anchoClase)
            intervalos[2].append(0)
        for i in self.l:
            for j in range(m):
                if intervalos[0][j] <= i < intervalos[1][j]:
                    intervalos[2][j] += 1
                    break
                elif i == 1:
                    intervalos[2][m - 1] += 1
                    break
        for i in range(m):
            estChi += math.pow((freqEsperada - intervalos[2][i]), 2) / freqEsperada
        if estChi < chi:
            print(
                f"No se puede rechazar que el conjunto ri sigue una distribucion uniforme con un nivel de aceptacion de {(1 - alpha) * 100:.0f}%")
            result = True
        else:
            print("Se rechaza que el conjunto ri sigue una distribucion uniforme.")
            result = False
        return result

    def pIndependencia(self, alpha: float) -> bool:
        resultado = False
        corridas = []
        c0 = 1
        n = self.m
        n0 = 0
        n1 = 0
        for i in self.l:
            if i >= 1/2:
                corridas.append(1)
                n1 += 1
            else:
                corridas.append(0)
                n0 += 1
        actual = corridas[0]
        for i in range(self.m):
            if corridas[i] != actual:
                c0 += 1
                actual = corridas[i]
        valorEsp = ((2 * n0 * n1) / n) + (1 / 2)
        var = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (math.pow(n, 2) * (n - 1))
        z0 = (c0 - valorEsp) / (math.sqrt(var))
        z = abs(st.norm.ppf(alpha / 2))
        if (-1)*z < z0 < z:
            print(
                f"No se puede rechazar que el conjunto de ri es independiente con un nivel de aceptacion de {(1 - alpha) * 100:.0f}%")
            resultado = True
        else:
            print("Los numeros del conjunto ri no son independientes.")
            resultado = False
        return resultado
