import PySimpleGUI as psg
import Simulacion
import Dados
import Camiones
import gVaral


def main():
    psg.theme('BlueMono')

    layoutPseudos = []
    layoutDados = []
    layoutCamiones = []
    layoutGVarAl = []

    tab1 = psg.Tab('Numeros pseudoaleatorios', layoutPseudos, key='pseudo')
    tab2 = psg.Tab('Dados', layoutDados,
                   element_justification='center', key='dados')
    tab3 = psg.Tab('Camiones', layoutCamiones,
                   element_justification='center', key='camiones')
    tab4 = psg.Tab('Generar Variables', layoutGVarAl,
                   element_justification='center', key='gvaral')

    layout = [
        [psg.TabGroup([[tab1, tab2, tab3, tab4]])]
    ]

    layoutPseudos = [
        [psg.Text('Introduzca los parametros: ',
                  justification='center', font='Calibri 15')],
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
        [psg.Button('Ok', size=(15, 1), key='generar', button_color=('black', 'white')),
         psg.Button('Resultados', size=(15, 1), key='resultados',
                    button_color=('black', 'white')),
         psg.Button('Close', size=(15, 1), key='close', button_color=('black', 'white'))]
    ]

    layoutDados = [
        [psg.Text('Lanzamientos por replica: ', size=20, font='Calibri 12'),
         psg.InputText(size=5, key='lanzamientos')],
        [psg.Text('Replicas: ', size=20, font='Calibri 12'),
         psg.InputText(size=5, key='replicasDados')],
        [psg.Button('Correr Simulacion', size=(15, 1), key='simudado', button_color=('black', 'white')),
         psg.Button('Intervalo de confianza', size=(15, 1), key='interval', button_color=('black', 'white'))],
        [psg.Button('Close', size=(15, 1),
                    key='close', button_color=('black', 'white'))]
    ]

    layoutCamiones = [
        [psg.Text('Empleados: ', size=20, font='Calibri 12'),
         psg.InputText('3', size=5, key='empleados')],
        [psg.Text('Costo espera camion: ', size=20, font='Calibri 12'),
         psg.InputText('100', size=5, key='cespcam')],
        [psg.Text('Salario: ', size=20, font='Calibri 12'),
         psg.InputText('25', size=5, key='salario')],
        [psg.Text('Tiempo extra: ', size=20, font='Calibri 12'),
         psg.InputText('37.5', size=5, key='tiempoextra')],
        [psg.Text('Costo Almacen: ', size=20, font='Calibri 12'),
         psg.InputText('500', size=5, key='costoalmacen')],
        [psg.Text('Replicas: ', size=6, font='Calibri 12'), psg.InputText('10', size=5, key='replicasCamiones'), psg.Button(
            'Correr Simulacion', size=(15, 1), key='simucamion', button_color=('black', 'white'))],
        [psg.Button('Close', size=(15, 1), key='close',
                    button_color=('black', 'white'))]
    ]

    layoutPoisson = [
        [psg.Text('lambda: ', size=5, font='Calibri 10'),
         psg.InputText(size=3, key='lambda')],
        [psg.Text('Cantidad: ', size=6, font='Calibri 10'),
         psg.InputText(size=3, key='pcant')],
        [psg.Button('Poisson', size=(15, 1), key='poisson',
                    button_color=('black', 'white'))],
        # [psg.Listbox(values=[], enable_events=True,
        #             size=(20, 10), key="tpoisson")],
        [psg.Button('Prueba', size=(15, 1), key='ppoisson',
                    button_color=('black', 'white'))]
    ]
    layoutNormal = [
        [psg.Text('mu: ', size=2, font='Calibri 10'), psg.InputText(size=3, key='mu'), psg.Text(
            'desv: ', size=3, font='Calibri 10'), psg.InputText(size=3, key='s')],
        [psg.Text('Cantidad: ', size=6, font='Calibri 10'),
         psg.InputText(size=3, key='ncant')],
        [psg.Button('Normal', size=(15, 1), key='normal',
                    button_color=('black', 'white'))],
        # [psg.Listbox(values=[], enable_events=True,
        #             size=(20, 10), key='tnormal')],
        [psg.Button('Prueba', size=(15, 1), key='pnormal',
                    button_color=('black', 'white'))]
    ]
    layoutGVarAl = [
        [psg.Column(layoutPoisson, element_justification='center'), psg.VSeparator(),
         psg.Column(layoutNormal, element_justification='center')],
        [psg.Button('Close', size=(15, 1), key='close',
                    button_color=('black', 'white'))]
    ]

    window = psg.Window('Sistema Simulacion', layout)

    tab1.Layout(layoutPseudos)
    tab2.Layout(layoutDados)
    tab3.Layout(layoutCamiones)
    tab4.Layout(layoutGVarAl)

    msg = []

    while True:
        event, values = window.read()  # type: ignore
        if event == 'close' or event == psg.WIN_CLOSED:
            break

        if event == 'pseudo':
            window['pseudo'].update(visible=True)
            window['dados'].update(visible=False)
            window['camiones'].update(visible=False)
            window['gvaral'].update(visible=False)
        elif event == 'dados':
            window['pseudo'].update(visible=False)
            window['dados'].update(visible=True)
            window['camiones'].update(visible=False)
            window['gvaral'].update(visible=False)
        elif event == 'camiones':
            window['pseudo'].update(visible=False)
            window['dados'].update(visible=False)
            window['camiones'].update(visible=True)
            window['gvaral'].update(visible=False)
        elif event == 'gvaral':
            window['pseudo'].update(visible=False)
            window['dados'].update(visible=False)
            window['camiones'].update(visible=False)
            window['gvaral'].update(visible=True)

        if event == 'generar':
            try:
                seed = int(values['seed'])
                g = int(values['g'])
                k = int(values['k'])
                c = int(values['c'])
                alpha = float(values['alpha'])
                msg = Simulacion.pseudoRandNumbers(seed, g, k, c, alpha)
                psg.popup("Resultados pruebas", msg[0], msg[1], msg[2], msg[3])
            except:
                men = 'Error en los datos ingresados'
                try:
                    if int(values['g']) == 1:
                        men += '\n g debe ser mayor a 1'
                except:
                    pass
                psg.popup(men)
        if event == 'resultados':
            try:
                psg.popup("Resultados pruebas", msg[0], msg[1], msg[2], msg[3])
            except:
                psg.popup("Para generar numeros hay que ingresar datos")

        if event == 'simudado':
            try:
                lanz = int(values['lanzamientos'])
                replicas = int(values['replicasDados'])
                msg = Dados.dados(lanz, replicas)
            except:
                psg.popup("Se requieren datos para simular")
                msg = 'Ingresar datos primero'
        if event == 'interval':
            psg.popup("Intervalos de confianza", msg)

        if event == 'simucamion':
            try:
                Camiones.camiones(int(values['empleados']), float(values['cespcam']), float(
                    values['salario']), float(values['tiempoextra']), float(values['costoalmacen']), int(values['replicasCamiones']))
            except:
                psg.popup("Se requieren datos para simular")

        if event == 'poisson':
            try:
                num = [gVaral.gPoisson(int(values['lambda']))
                    for i in range(int(values['pcant']))]
                gVaral.writeNumbers(num, 'data_GVarAl/Poisson/gPoisson')
                msg = gVaral.testPoisson(num, int(values['lambda']))
            except:
                psg.popup("Error en los datos")
                msg = ['Error','no hay datos']
        if event == 'ppoisson':
            try:
                psg.popup("Resultados pruebas", msg[0], msg[1])
            except:
                psg.popup("Para poder hacer una prueba hay que generar numeros")

        if event == 'normal':
            try:
                num = [gVaral.gNorm(float(values['mu']), float(values['s']))
                    for i in range(int(values['ncant']))]
                gVaral.writeNumbers(num, 'data_GVarAl/Normal/gNormal')
                msg = gVaral.testNormal(num, float(
                    values['mu']), float(values['s']))
            except:
                psg.popup("Error en los datos")
                msg = ['Error','no hay datos']
        if event == 'pnormal':
            try:
                psg.popup("Resultados pruebas", msg[0], msg[1])
            except:
                psg.popup("Para poder hacer una prueba hay que generar numeros")

    window.close()


if __name__ == "__main__":
    main()
