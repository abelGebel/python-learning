"""
Enuncuado:
En una carpeta que contiene ficheros .pdf, proteger cada fichero con una contraseña.
"""

import os # Para trabajar con rutas de archivos.
import glob # Para buscar archivos o directorios que coincidad con un patron especifico.
from PyPDF2 import PdfReader, PdfWriter

folder = r"C:\Users\abelg\OneDrive\Escritorio\python-learning\02_Challenges\PDF" # Especificamos la ruta de los pdfs.
patron = "*.pdf" # Establecemos el patron a buscar.

archivos_pdf = glob.glob(os.path.join(folder, patron)) # Con la funcion .glob buscamos archivos en una carpeta especifica que correspondan a un patron especificado.

for archivo_pdf in archivos_pdf: # Iteramos a traves de ese listado de archivos y creamos dos objetos (reader y writer).
    reader = PdfReader(archivo_pdf)
    writer = PdfWriter()

    for page in reader.pages: # Iteramos por cada una de las paginas de los pdfs y las escribimos en writer
        writer.add_page(page)

        writer.encrypt("password") # Especificamos la contraseña

        with open(archivo_pdf, "wb") as f: # Sobreescribimos ese archivo con la version cifrada
            writer.write(f)

