# Conversión de reportes
Estos scripts son utilizados para convertir los reportes de ausentismo y comedor de netTime al formato necesario para liquidación.

## Instalar Python >= 3.8 ##
1. Descargar la versión más reciente del intérprete de Python desde el siguiente [Enlace](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe "Python Downloads").

2. Instalar agregando al PATH en el proceso de instalación.


## Configurar nombres de archivos ##
1. Chequear o modificar el nombre del archivo a procesar en el archivo settings.py dentro de la carpeta correspondiente

``` python
├── ...
├── pg-convert/				# Directorio base
│   ├── convert_ausentismo/		# Procesamiento de ausentismo
│	│	├── Pending/		# Incluir el file a convertir
│	│	├── Done/		# Archivos generados con scripts
│	│	├── settings.py 
│	│	└── convert.py	# Config de nombres de E/S
│   └── convert_comedor/    		# Procesamiento de comedor
│		├── Pending/
│		├── Done/
│		├── settings.py
│		└── convert.py
└── ...
```

