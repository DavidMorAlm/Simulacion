from Pseudo import Pseudo
import PySimpleGUI as psg

def pseudoRandNumbers():
    # Inicializacion de parámetros
    x0, g, k, c, alfa, = 0, 0, 0, 0, 0


    #  Definicion de la ventana
    psg.theme('BlueMono')
    layout = [
        [psg.Text('Introduzca los parametros: ', justification='center', font='Calibri 15')],
        [psg.Text('Seed: ', justification='right', size=(6, 1), font='Calibri 12'),
        psg.InputText(size=5, key='seed')],
        [psg.Text('g: ', justification='right', size=(6, 1), font='Calibri 12'),
        psg.InputText(size=5, key='g')],
        [psg.Text('k: ', justification='right', size=(6, 1), font='Calibri 12'),
        psg.InputText(size=5, key='k')],
        [psg.Text('c: ', justification='right', size=(6, 1), font='Calibri 12'),
        psg.InputText(size=5, key='c')],
        [psg.Text('alpha: ', justification='right', size=(6, 1), font='Calibri 12'),
        psg.InputText('0.05', size=5, key='alpha')],
        [psg.Button('Close', size=(15, 1), key='close', button_color=('black', 'white')),
        psg.Button('Ok', size=(15, 1), key='ok', button_color=('black', 'white'))],
    ]
    ventana = psg.Window('Generar Números Aleatorios', layout, enable_close_attempted_event=True)

    while True:
        event, values = ventana.read()  # type: ignore
        if event in 'close':
            break
        elif event in 'ok':
            x0 = int(values['seed'])
            g = int(values['g'])
            k = int(values['k'])
            c = int(values['c'])
            alfa = float(values['alpha'])
            break

    ventana.close()


    # Parametros iniciales para generar los numeros pseudo-aleatorios
    # x0 = 6  g = 13  k = 15  c = 8191  alfa = 0.05


    # Se generan los pseudo y se les aplican cada una de las pruebas correspondientes
    n = Pseudo(x0, g, k, c)
    n.gLineal()
    n.pMedias(alfa)
    n.pVarianza(alfa)
    n.pUniformidad(alfa)
    n.pIndependencia(alfa)
