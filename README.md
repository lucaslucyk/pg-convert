# Conversión de reportes
Estos scripts son utilizados para convertir los reportes de ausentismo y comedor de netTime al formato necesario para liquidación.

## Descargar y descomprimir ##
1. Descargar `ZIP` del repositorio y descomprimir en el directorio deseado. 
![Download 1](statics/dl_repo.png?raw=true "Download")

*Se recomienda no descomprimir en el disco `C:\` directamente.*

## Instalar Python3 ##
1. Descargar la versión más reciente del intérprete de Python desde el siguiente [Enlace](https://www.python.org/ "Python Downloads").
![Download 1](statics/dl_01.png?raw=true "Download")
![Download 2](statics/dl_02.png?raw=true "Download")

2. Instalar agregando al PATH en el proceso de instalación.
![Instalacion path](statics/in_01.png?raw=true "Instalación")

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
│   │   │   └── ausentismo_nt.csv   # Por defecto           
│   │   └── ...
│   └── convert_comedor/
│       ├── Pending/
│       │   └── comedor_nt.csv      # Por defecto    
│       └── ...
└── ...
```

3. Luego de ubicar el archivo en el directorio correspondiente, ejecutar el archivo `convert.py` y buscar el archivo generado dentro de la carpeta `Done`.

```
├── ...
├── pg-convert/                 
│   ├── convert_ausentismo/    
│   │   ├── Done/
│   │   │   └── ausentismo.csv   # Por defecto           
│   │   └── ...
│   └── convert_comedor/
│       ├── Done/
│       │   └── comedor.csv      # Por defecto    
│       └── ...
└── ...
```

4. El archivo generado ya puede ser abierto desde Excel o cualquier editor de texto.

*En caso de usar Windows, considerar no ubicar los scripts dentro del disco `C:\` directamente, o en tal caso, ejecutar con permisos de Adminitrador.*