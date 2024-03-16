import PyPDF2

lector_pdf = PyPDF2.PdfReader('.pdf')
lector_firma = PyPDF2.PdfReader('firma.pdf')
escritor_pdf = PyPDF2.PdfWriter()

pagina_actual = lector_pdf.pages[0] # Primera pagina
lector_firma.pages[0].add_transformation(PyPDF2.Transformation().translate(-50, -450))
pagina_actual.merge_page(lector_firma.pages[0])
escritor_pdf.add_page(pagina_actual)

nombre_salida = "pdf_firmado.pdf"
with open(nombre_salida, 'wb')as salidad:
    escritor_pdf.write(salidad)