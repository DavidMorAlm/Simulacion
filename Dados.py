import statistics as sts
from Simulacion import n


def media(numeros):
    return sum(numeros) / len(numeros)


def mediana(numeros):
    n = len(numeros)
    num = sorted(numeros)
    if n % 2 == 0:
        return (num[n // 2] + num[n // 2 - 1]) / 2
    else:
        return num[n // 2]


def moda(numeros):
    return max(set(numeros), key=numeros.count)


def varianza(numeros):
    mu = media(numeros)
    return sum((x - mu) ** 2 for x in numeros) / len(numeros)


def desviacion(numeros):
    return varianza(numeros) ** 0.5


# Ejercicio dados
with open("Dados.csv", "w") as archivo:
    archivo.write("Corrida,Datos,Media,Mediana,Moda,S,S^2")
j = 1
lanzamientos = 50

for i in range(1, 11):
    with open("Dados.csv", "a") as archivo:
        archivo.write(f"\n{i},{j}-{lanzamientos}")
    numeros = []
    for a in range(j, lanzamientos + 1):
        pseudo = n.l[a - 1]
        if 0 <= pseudo < 1/6:
            x = 1
            numeros.append(x)
        elif 1/6 <= pseudo < 2/6:
            x = 2
            numeros.append(x)
        elif 2/6 <= pseudo < 3/6:
            x = 3
            numeros.append(x)
        elif 3/6 <= pseudo < 4/6:
            x = 4
            numeros.append(x)
        elif 4/6 <= pseudo < 5/6:
            x = 5
            numeros.append(x)
        else:
            x = 6
            numeros.append(x)
    with open("Dados.csv", "a") as archivo:
        archivo.write(
            f",{media(numeros)},{mediana(numeros)},{moda(numeros)},{desviacion(numeros):.4f},{varianza(numeros):.4f}")
    j += 50
    lanzamientos += 50
