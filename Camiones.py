from Simulacion import n
import Transformada as ti
import statistics as sts
import datetime
from fractions import Fraction


# Ejercicio camiones
l = n.l.copy()
t = open("tiCamiones.csv", "r")
with open("Camiones.csv", "w") as f:
    f.write(
        "#pse,Numero camion,#pse,Hora de llegada,Hora de entrada a descarga,#pse,Tiempo de descarga,Hora de salida del camion,Tiempo de espera\n")


# Condiciones iniciales
'''
    Equipo: 3 personas
    Turno: 8 horas
    Horario: 11:00 pm - 07:30 am
    Comida: 03:00 am . 03:30 am
    Nota: Se termina de descargar el camion y despues se toman alimentos si es que el camion se descarga durante el horario de la comida
'''
horaInicio = datetime.datetime(100, 1, 1, 23, 0)
horaFin = datetime.datetime(100, 1, 2, 7, 30)
horaComida = datetime.datetime(100, 1, 1, 3, 0)
horaFinComida = datetime.datetime(100, 1, 1, 3, 30)
horaAct = horaInicio

# Almacenar las tablas de probabilidades.
a, b = ti.leerTi(t)  # Numero de camiones en espera antes de abrir
c, d = ti.leerTi(t)  # Tiempo de entre llegadas
e, o = ti.leerTi(t)  # Tiempo de servicio (3 personas)
g, h = ti.leerTi(t)  # Tiempo de servicio (4 personas)
i, j = ti.leerTi(t)  # Tiempo de servicio (5 personas)
m, n = ti.leerTi(t)  # Tiempo de servicio (6 personas)


# Simular el numero de camiones en cola antes de que abra el negocio.
f = open("Camiones.csv", "a")


# Verificar el primer camion en ingresar al almacen.
pse = round(l.pop(0), 4)
numCamiones = ti.gTi(a, b, pse)
f.write(f"{pse},{numCamiones},")
if numCamiones == 0:    # Si no hay camiones en espera, antes de que se abra el negocio.
    pse = round(l.pop(0), 4)
    horaLleg = horaAct + datetime.timedelta(minutes=ti.gTi(c, d, pse))  # type: ignore
    horaAct = horaLleg
    horaEntrada = horaLleg
    f.write(f"{pse},{horaLleg.time().isoformat('minutes')},{horaEntrada.time().isoformat('minutes')},")
    pse = round(l.pop(0), 4)
    tiempoDescarga = ti.gTi(e, o, pse)
    horaSalida = horaEntrada + datetime.timedelta(minutes=tiempoDescarga)  # type: ignore
    tiempoEsp = horaEntrada - datetime.timedelta(hours=horaLleg.time().hour, minutes=horaLleg.time().minute) 
    f.write(f"{pse},{tiempoDescarga},{horaSalida.time().isoformat('minutes')},{tiempoEsp.time().isoformat('minutes')}\n")
else:   #En caso de que haya camiones en espera.
    print("Hay camiones en espera antes de que se abra el negocio.")


# Simular el resto de los camiones.    
while(horaAct < horaFin):
    pse = round(l.pop(0), 4)
    horaLleg = horaAct + datetime.timedelta(minutes=ti.gTi(c, d, pse))  # type: ignore
    horaAct = horaLleg
    if horaSalida.time() == horaComida.time():
        horaSalida = horaFinComida
    if horaSalida.time() <= horaLleg.time():  # type: ignore
        horaEntrada = horaLleg
    else:
        horaEntrada = horaSalida
    f.write(f",,{pse},{horaLleg.time().isoformat('minutes')},{horaEntrada.time().isoformat('minutes')},") # type: ignore
    pse = round(l.pop(0), 4)
    tiempoDescarga = ti.gTi(e, o, pse)
    horaSalida = horaEntrada + datetime.timedelta(minutes=tiempoDescarga)  # type: ignore
    tiempoEsp = horaEntrada - datetime.timedelta(hours=horaLleg.time().hour, minutes=horaLleg.time().minute) # type: ignore
    f.write(f"{pse},{tiempoDescarga},{horaSalida.time().isoformat('minutes')},{tiempoEsp.time().isoformat('minutes')}\n")  # type: ignore



f.close()
