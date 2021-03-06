from datetime import datetime

today = datetime.today()

print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))

print("La hora actual es {}".format(today.hour))
print("El minuto actual es {}".format(today.minute))
print("El segundo actual es {}".format(today.second))

now = datetime.now()
format1 = now.strftime('Día :%d, Mes: %m, Año: %Y')
format2 = now.strftime('Hora: %H, Minutos: %M, Segundos: %S')
print(format1)
print(format2)
