"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 """


import requests
from PIL import Image
from io import BytesIO

def calcular_aspect_ratio(url):
    # Realizar solicitud GET para obtener la imagen desde la URL
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Leer la imagen desde la respuesta y abrirla con PIL
        imagen = Image.open(BytesIO(response.content))
        
        # Obtener las dimensiones de la imagen
        ancho, altura = imagen.size
        
        # Calcular el aspect ratio
        ratio = ancho / altura
        
        return ratio
    else:
        print("Error al descargar la imagen. Código de estado:", response.status_code)
        return None

# URL de ejemplo
url_ejemplo = "https://files.soniccdn.com/images/articles/amp/37887.jpg"

# Calcular el aspect ratio
aspect_ratio = calcular_aspect_ratio(url_ejemplo)

# Imprimir el resultado
if aspect_ratio:
    print("Aspect ratio de la imagen:", aspect_ratio)
