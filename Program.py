import Simulacion
import Dados
import Camiones
import gVaral


def main():
    # Generar numeros pseudoaleatorios, guardarlos en el archivo 'Numeros.csv'
    Simulacion.pseudoRandNumbers()
    # Ejercicio dados
    Dados.dados()
    # Ejercicio camiones
    Camiones.camiones()


if __name__ == "__main__":
    main()