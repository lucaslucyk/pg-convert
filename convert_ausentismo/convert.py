import csv, datetime, os, settings

'''
empleados = {
	empleado : {
		dias : [d1, d2, ...],
		intervalos : [[ini, fin, cant], [ini, fin, cant], ...],
	}
}
'''

empleados = {}

with open(f'Pending\\{settings.FILE_TO_PROCESS}', mode='rU') as file:
	reader = csv.reader(file, delimiter=';')

	for n, row in enumerate(reader):
		if not n:
			continue

		empleado, concepto, dia, cant = row

		if empleado not in empleados:
			empleados[empleado] = dict()

		if concepto not in empleados[empleado]:
			empleados[empleado][concepto] = dict()
			empleados[empleado][concepto]["dias"] = list()
			empleados[empleado][concepto]["intervalos"] = list()

		empleados[empleado][concepto]["dias"].append(datetime.datetime.strptime(dia, '%d/%m/%Y'))

lineas_to_print = []

for empleado, v in empleados.items():
	for concepto, k in v.items():
		if "intervalos" not in k.keys():
				k["intervalos"] = list()

		if len(k["dias"]) == 1:
			k["intervalos"].append([k["dias"][0], k["dias"][0], 1])
		else:
			for dia in k["dias"]:
				if not len(k.get("intervalos")):
					k["intervalos"].append([dia, dia, 1])
				else:
					if (dia - k["intervalos"][-1][1]).days == 1:
						k["intervalos"][-1][1] = dia
						k["intervalos"][-1][2] += 1
					else:
						k["intervalos"].append([dia, dia, 1])

		for intervalo in k["intervalos"]:
			lineas_to_print.append((
				"FQ", 
				"1",
				"2001",
				empleado,
				"",
				concepto,
				intervalo[0].strftime('%Y%m%d'),
				intervalo[1].strftime('%Y%m%d')
				))

with open(f"Done\\{settings.FILE_OUT}", "w", newline="") as out:
    writer = csv.writer(out, delimiter=';')
    writer.writerows(lineas_to_print)

newFileName = f'{settings.FILE_TO_PROCESS.rstrip(".csv")}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
os.rename(f'Pending\\{settings.FILE_TO_PROCESS}', f'Pending\\Back\\{newFileName}')


