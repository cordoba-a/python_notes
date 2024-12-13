Extracción de Datos desde Imágenes con Python

Este proyecto contiene un script en Python que procesa una imagen de una lista de estudiantes (captura de un documento original en PDF) y extrae las columnas de interés: matrícula y nombre. Posteriormente, los datos se guardan en un archivo CSV.

Requisitos Previos

Tener instalado Python 3.6 o superior.

Instalar las siguientes bibliotecas necesarias:

pip install pytesseract pillow pandas

En macOS, instala Tesseract OCR con:

brew install tesseract

Descripción del Proceso

Captura de imagen:

Se capturó una imagen que contiene las columnas de interés (matrícula y nombre del alumno) a partir de un documento PDF original.

Procesamiento del texto:

El script utiliza Tesseract OCR para extraer el texto de la imagen.

Se limpian y separan las matrículas y los nombres de los estudiantes con expresiones regulares.

Creación de DataFrames:

Los datos extraídos se organizan en columnas utilizando la biblioteca pandas.

Exportación de resultados:

El resultado final se guarda en un archivo CSV llamado datos_extraidos.csv.

Uso

1. Modifica la ruta de la imagen

Actualiza la variable image_path con la ruta completa donde se encuentra tu imagen:

image_path = "ruta/a/tu/imagen.png"

2. Ejecuta el script

Ejecuta el código proporcionado en tu entorno de Python.

3. Resultado

El script generará un archivo llamado datos_extraidos.csv con el siguiente formato:

No.

Matrícula

Nombre alumno

1

244020028

BRETON NICASIO DIEGO ALEJANDRO

2

244020007

CARREON ROSALES MARGARITA

...

...

...

