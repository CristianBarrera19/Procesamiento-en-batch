# Medicamentos En Colombia

## Descripcion
Esta actividad implementa un proceso de análisis de datos en batch utilizando Apache Spark y Python, se trabaja con un conjunto de datos real sobre precios de medicamentos en Colombia, obtenido desde un sitio oficial de datos abiertos.

El objetivo es aplicar técnicas de limpieza, transformación y análisis exploratorio de datos para obtener información importante sobre los precios de medicamentos en Colombia.

## Fuente de Datos
Datos Abiertos Colombia  
https://www.datos.gov.co/Salud-y-Protecci-n-Social/Precios-Medicamentos/3t73-n4q9/about_data

## Herramientas Usadas
* VirtualBox
* Putty
* Apache Spark
* Python
* Comandos(nano, wget, spark-submit)

## Procedimiento
1. Abrir entorno VirtualBox
2. iniciar sesion con:
   Usuario: vboxuser
   Password: bigdata
3. Copiar Ipv4
4. Abrir Putty
5. Pegar Ip en HostName
6. Iniciar Hadoop con:
   Usuario: Hadoop
   Password: Hadoop
7. Descargar CSV en maquina virtual con comando:
   wget https://www.datos.gov.co/resource/3t73-n4q9.csv
8. Configurar entorno batch con comando:
   nano batch_medicamentos.py
9. Ejecutar batch con comando:
   spark-submit batch_medicamentos.py
10. Se ejecutara en pantalla el analisis de los datos

## Descripcion de Solucion
Se basa en el desarrollo de un proceso de análisis de datos en batch utilizando Apache Spark con python, aplicado a un conjunto de datos de precios de medicamentos en Colombia.

Se realiza la carga del dataset, la limpieza de datos eliminando valores nulos y la transformación de variables para su correcto análisis, despues de esto se ejecuta un análisis exploratorio que incluye el cálculo de métricas como promedio, máximo, mínimo y conteo de registros, así como la identificación de los medicamentos más costosos y el cálculo del precio promedio por producto.

Los resultados se muestran en consola, mostrando el uso de Apache Spark como herramienta para el procesamiento de grandes volúmenes de datos
