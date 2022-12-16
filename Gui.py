import PySimpleGUI as sg

def createTable(path: str, name: str) -> None:
    with open(path,'r') as f:
        headings = [[s] for s in f.readline().removesuffix('\n').replace(' ', '_').split(',')]
        value  = [[[v] for v in s.removesuffix('\n').replace(' ', '_').split(',')] for s in f.readlines()]

    sg.theme('DarkAmber')

    layout = [
            [sg.Table(values=value, headings=headings, max_col_width=35,
                        auto_size_columns=True,
                        justification='right',
                        num_rows=10,
                        key='-TABLE-',
                        row_height=35)]
        ]

    window = sg.Window('Tabla ' + name, layout, modal=True)

    while True:
        event, values = window.read() # type: ignore
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()

def createList(path: str, name: str) -> None:
    with open(path,'r') as f:
        value  = [s.removesuffix('\n') for s in f.readlines()]

    sg.theme('DarkAmber')

    layout = [
            [sg.Listbox(values=value, size=(20, 20), key='-LIST-', enable_events=True)]
        ]

    window = sg.Window('Lista ' + name, layout, modal=True)

    while True:
        event, values = window.read() # type: ignore
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()