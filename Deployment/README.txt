README
===================================
Autor: Diego Valladares
Fecha: 30/12/2021
Lenguaje: Python 3.9.0

============ LIBRERÍAS ==============
pip	 : 21.1.2
pandas 	 : 1.2.0	 => pip install pandas
argparse:  	=>  pip install argparse

============ OUTPUT ==============
Se debe crear carpeta output en el directorio de ejecución de python para obtener resultados

- The top 10 best games for each console/company.
- The worst 10 games for each console/company.
- The top 10 best games for all consoles.
- The worst 10 games for all consoles

============ DATA ==============
En el mismo directorio donde se ejecutará el script de python, deben estar los siguientes archivos en la carpeta data:

- consoles.csv
- result.csv

============ ESTRUCTURA DE CARPETAS/ARCHIVOS PARA LA EJECUCIÓN DE SCRIPT ==============
C:.
│   main.py
│   README.txt
│
├───data
│       consoles.csv
│       result.csv
│
└───output

============ EJECUCIÓN ==============

py main.py => ejecución de script por defecto
py main.py --h => descripción de argumentos opcionales

py main.py -r CANTIDAD_FILAS_A_MOSTRAR, ej: py main.py -r 20
py main.py -f COLUMNA_A_ORDERNAR, ej: py main.py -f metascore

py main.py -r 30 -f metascore

============ DOCKER  ==============
docker build -t docker-walmart .
docker images
docker run -v D:\output:/output docker-walmart python main.py



