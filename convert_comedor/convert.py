import csv, datetime, os, settings

'''
empleados = {
	empleado : [marc_1, marc_2, ...],
}

1690265;07/01/2020;07/02/2020;07/01/2020 0:09:07;1;P9266523 
 

'''

empleados = {}
centros = {}

fecha_ini, fecha_fin = None, None

with open(f'Pending\\{settings.FILE_TO_PROCESS}', mode='rU') as file:
	reader = csv.reader(file, delimiter=';')

	for n, row in enumerate(reader):
		if not n:
			continue

		empleado, fechaIni, fechaFin, fecha_marc, cont, cc = row

		if not fecha_ini and not fecha_fin:
			fecha_ini = datetime.datetime.strptime(fechaIni, '%d/%m/%Y')
			fecha_fin = datetime.datetime.strptime(fechaFin, '%d/%m/%Y')

		if empleado not in empleados:
			empleados[empleado] = list()

		if empleado not in centros:
			centros[empleado] = cc
		
		fecha = datetime.datetime.strptime(fecha_marc, '%d/%m/%Y %H:%M:%S')

		if not len(empleados.get(empleado)):
			empleados[empleado].append(fecha)
		else:
			empleados[empleado].append(fecha) if abs((fecha - empleados[empleado][-1]).total_seconds()) >= 14400 else None

lineas_to_print = []

for empleado, marcajes in empleados.items():
	lineas_to_print.append((
		'F2',
		'3',
		'15',
		empleado,
		'',
		(fecha_fin - datetime.timedelta(days=1) ).strftime('%Y%m%d'),
		(fecha_fin - datetime.timedelta(days=1) ).strftime('%Y%m%d'),
		'4118',
		str(len(marcajes)),
		'Unit',
		'',
		'AR',
		centros.get(empleado),
		'501',
	))

with open(f"{settings.FILE_OUT}", "w", newline="") as out:
    writer = csv.writer(out, delimiter=';')
    writer.writerows(lineas_to_print)

newFileName = f'{settings.FILE_TO_PROCESS.rstrip(".csv")}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
os.rename(f'Pending\\{settings.FILE_TO_PROCESS}', f'Done\\{newFileName}')


