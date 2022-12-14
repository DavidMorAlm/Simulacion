from Pseudo import Pseudo
import PySimpleGUI as psg

def pseudoRandNumbers(seed: int, g: int, k: int, c: int, alfa: float) -> list:
    # Parametros iniciales para generar los numeros pseudo-aleatorios
    # seed = 6  g = 13  k = 15  c = 8191  alfa = 0.05


    # Se generan los pseudo y se les aplican cada una de las pruebas correspondientes
    n = Pseudo(seed, g, k, c)
    n.gLineal()
    n.pMedias(alfa)
    n.pVarianza(alfa)
    n.pUniformidad(alfa)
    n.pIndependencia(alfa)

    return n.msg