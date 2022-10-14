import PySimpleGUI as psg


psg.theme('BlueMono')
layout = [
    [psg.Text('Introduzca los parametros: ', font='Calibri 20')],
    [psg.Text('Semilla: ', size=(15, 1), font='Calibri 12'),
     psg.InputText(key='seed')],
    [psg.Text('g: ', size=(15, 1), font='Calibri 12'), psg.InputText(key='g')],
    [psg.Text('k: ', size=(15, 1), font='Calibri 12'), psg.InputText(key='k')],
    [psg.Text('c: ', size=(15, 1), font='Calibri 12'), psg.InputText(key='c')],
    [psg.Text('alpha: ', size=(15, 1), font='Calibri 12'),
     psg.InputText(key='alpha')],
    [psg.Button('Close', size=(20, 1), key='close', button_color=('black', 'white')),
     psg.Button('Ok', size=(20, 1), key='ok', button_color=('black', 'white'))],
]

ventana = psg.Window('Generar Números Aleatorios', layout, enable_close_attempted_event=True)

while True:
    event, values = ventana.read()  # type: ignore
    # The line of code to save the position before exiting
    if event in (psg.WINDOW_CLOSE_ATTEMPTED_EVENT, 'close'):
        break
    elif event in ('ok'):
        x0 = int(values['seed'])
        g = int(values['g'])
        k = int(values['k'])
        c = int(values['c'])
        alfa = float(values['alpha'])
        break

ventana.close()
