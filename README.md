# Conversión de reportes
Estos scripts son utilizados para convertir los reportes de ausentismo y comedor de netTime al formato necesario para liquidación.

## Instalar Python >= 3.8 ##
1. Descargar la versión más reciente del intérprete de Python desde el siguiente [Enlace](https://www.python.org/downloads/ "Python Downloads").

2. Instalar agregando al PATH en el proceso de instalación.


## Configurar nombres de archivos ##
1. Chequear o modificar el nombre del archivo a procesar en el archivo settings.py dentro de la carpeta correspondiente

```
├── ...
├── pg-convert/                 # Directorio base
│    ├── convert_ausentismo/    # Procesamiento de ausentismo
│    │    ├── Pending/          # Incluir el file a convertir
│    │    ├── Done/             # Archivos generados con scripts
│    │    ├── settings.py       # Config de nombres de E/S de Ausentismo
│    │    └── convert.py        # Ejecutable para procesar Ausentismo
│    └── convert_comedor/       # Procesamiento de comedor
│        ├── Pending/
│        ├── Done/
│        ├── settings.py        # Config de nombres de E/S de Comedor
│        └── convert.py         # Ejecutable para procesar Comedor
└── ...
```

En el settings, se puede modificar el valor del nombre del archivo a procesar con la variable `FILE_TO_PROCESS` y el nombre del archivo que se generará con la variable `FILE_OUT`.

2. Una vez verificado los nombres de archivos, ubicar el archivo dentro de la carpeta `Pending` del directorio correspondiente (ausentismo o comedor). 
```
├── ...
├── pg-convert/                 
│   ├── convert_ausentismo/    
│   │   ├── Pending/
│   │   │   └── ausentismo_nt.csv    # Por defecto           
│   │   └── ...
│   └── convert_comedor/
│       ├── Pending/
│       │   └── comedor_nt.csv    # Por defecto    
│       └── ...
└── ...
```
