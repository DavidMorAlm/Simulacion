import statistics as sts
from Leer import leerNum
from scipy import stats
import Transformada as ti


def intervaloConfianza(list: list[float], alpha: float = 0.05):
    return stats.t.interval(1 - alpha, len(list) - 1, loc = sts.mean(list), scale = stats.sem(list))
    

def dados(lanz: int, replicas: int) -> list:
    # Ejercicio dados
    with open("TIs/tiDados.csv","r") as f:
        a, b= ti.leerTi(f)
    with open("data_Dados/Dados.csv", "w") as archivo:
        archivo.write("Corrida,Datos,Media,Mediana,Moda,S,S^2,Intervalo de Confianza")
    n = leerNum("data_Simulacion/Numeros.csv")
    j = 1
    lanzamientos = lanz
    intervals = []
    for i in range(1, replicas + 1):
        with open("data_Dados/Dados.csv", "a") as archivo:
            archivo.write(f"\n{i},{j}-{lanzamientos}")
        numeros =  [ti.gTi(a, b, n.pop(0)) for i in range(lanz)]
        with open("data_Dados/Dados.csv", "a") as archivo:
            interval = intervaloConfianza(numeros)
            intervals.append(interval)
            archivo.write(
                f",{sts.mean(numeros)},{sts.median(numeros)},{sts.mode(numeros)},{sts.pstdev(numeros):.4f},{sts.pvariance(numeros):.4f},[{interval[0]}-{interval[1]}]")  # type: ignore
        j += lanz
        lanzamientos += lanz
    return intervals