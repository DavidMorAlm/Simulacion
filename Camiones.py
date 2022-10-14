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
Empleados = 3
CostEsperaCamion = 100
Salario = 25
CostoNormal = 0
TiempoExtra = 37.5
CostoExtra = 0
CostoAlmacen = 500
CostTotal = 0

horaAct = horaInicio
horaSalida = 0
totalEsp = datetime.datetime(100, 1, 1, 0, 0)

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
    horaLleg = horaAct + \
        datetime.timedelta(minutes=ti.gTi(c, d, pse))  # type: ignore
    horaAct = horaLleg
    horaEntrada = horaLleg
    f.write(
        f"{pse},{horaLleg.time().isoformat('minutes')},{horaEntrada.time().isoformat('minutes')},")
    pse = round(l.pop(0), 4)
    tiempoDescarga = ti.gTi(e, o, pse)
    horaSalida = horaEntrada + \
        datetime.timedelta(minutes=tiempoDescarga)  # type: ignore
    tiempoEsp = horaEntrada - \
        datetime.timedelta(hours=horaLleg.time().hour,
                           minutes=horaLleg.time().minute)
    totalEsp = totalEsp + datetime.timedelta(
        hours=tiempoEsp.time().hour, minutes=tiempoEsp.time().minute)  # type: ignore
    f.write(f"{pse},{tiempoDescarga},{horaSalida.time().isoformat('minutes')},{tiempoEsp.time().isoformat('minutes')}\n")
else:  # En caso de que haya camiones en espera.
    print("Hay camiones en espera antes de que se abra el negocio.")


# Simular el resto de los camiones.
while (horaAct < horaFin):
    pse = round(l.pop(0), 4)
    horaLleg = horaAct + \
        datetime.timedelta(minutes=ti.gTi(c, d, pse))  # type: ignore
    horaAct = horaLleg
    if horaSalida.time() == horaComida.time():  # type: ignore
        horaSalida = horaFinComida
    if horaSalida.time() <= horaLleg.time():  # type: ignore
        horaEntrada = horaLleg
    else:
        horaEntrada = horaSalida   # type: ignore
    f.write(
        f",,{pse},{horaLleg.time().isoformat('minutes')},{horaEntrada.time().isoformat('minutes')},")  # type: ignore
    pse = round(l.pop(0), 4)
    tiempoDescarga = ti.gTi(e, o, pse)
    horaSalida = horaEntrada + \
        datetime.timedelta(minutes=tiempoDescarga)  # type: ignore
    tiempoEsp = horaEntrada - \
        datetime.timedelta(hours=horaLleg.time().hour,
                           minutes=horaLleg.time().minute)  # type: ignore
    totalEsp = totalEsp + datetime.timedelta(
        hours=tiempoEsp.time().hour, minutes=tiempoEsp.time().minute)  # type: ignore
    # type: ignore
    f.write(f"{pse},{tiempoDescarga},{horaSalida.time().isoformat('minutes')},{tiempoEsp.time().isoformat('minutes')}\n")

f.close()


# Calcular el costo total.
print(f"Tiempo de espera: {totalEsp.time()}")
CostEsperaCamion = (totalEsp.time().hour +
                    totalEsp.time().minute / 60) * CostEsperaCamion
CostTotal += CostEsperaCamion
print(f"Costo de espera del camion: ${CostEsperaCamion}")
horario = horaFin - \
    datetime.timedelta(hours=horaInicio.time().hour,
                       minutes=horaInicio.time().minute)
CostoNormal = horario.time().hour * Empleados * Salario
CostTotal += CostoNormal
print(f"Costo tiempo normal operadores: ${CostoNormal}")
CostoExtra = horaSalida - \
    datetime.timedelta(hours=horaFin.time().hour,
                       minutes=horaFin.time().minute)  # type: ignore
CostoExtra = CostoExtra.time().hour + CostoExtra.time().minute / 60  # type: ignore
if CostoExtra > 0:  # type: ignore
    CostoExtra = CostoExtra * Empleados * TiempoExtra  # type: ignore
    CostTotal += CostoExtra
    print(f"Costo tiempo extra operadores: ${CostoExtra}")
horario = horaSalida - datetime.timedelta(
    hours=horaInicio.time().hour, minutes=horaInicio.time().minute)  # type: ignore
horario = horario.time().hour + horario.time().minute / 60  # type: ignore
CostoAlmacen = horario * CostoAlmacen
CostTotal += CostoAlmacen
CostTotal = round(CostTotal, 3)
print(f"Costo disponibilidad del almacen: ${CostoAlmacen}")
print(f"Costo total: ${CostTotal}")
