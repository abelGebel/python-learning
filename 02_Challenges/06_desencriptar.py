import os
import glob
from PyPDF2 import PdfReader, PdfWriter

folder = r"C:\Users\abelg\OneDrive\Escritorio\python-learning\02_Challenges\PDF"
patron = "*.pdf"

archivos_pdf = glob.glob(os.path.join(folder, patron))

nueva_contraseña = ""

for archivo_pdf in archivos_pdf:
    reader = PdfReader(archivo_pdf)

    # Verificar si el archivo PDF ya está cifrado.
    if reader.is_encrypted:
        # Desencriptar el archivo PDF con la contraseña actual.
        reader.decrypt("password")

    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # Volver a cifrar el archivo PDF con la nueva contraseña, para qitar la contraseña colocar una cadena vacia "".
    writer.encrypt(nueva_contraseña)

    with open(archivo_pdf, "wb") as f:
        writer.write(f)