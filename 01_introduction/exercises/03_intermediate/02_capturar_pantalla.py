import cv2 # Para crear el video final
import numpy as np # Para crear el video final
import pyautogui # Para realizar la secuencia de prints
import keyboard # Capturar eventos del teclado

fps = 10.0 #Fotogramas por segundo
resolucion = pyautogui.size() # Reslución final del video

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Compresion para mp4
out = cv2.VideoWriter('grabacion.mp4',
                      fourcc,
                      fps, resolucion) # Objeto para crear el video de acuredo a los frames indicados

while True: # Ciclo para ir realizando las capturas
    frame = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame) # Escribe cada frame en el objeto VideoWriter creado

    if keyboard.is_pressed('q'): # Salir de la grabación con la tecla 'q'
        break

out.release() # Se guarda el video
cv2.destroyAllWindows() #Liberar los recursos

"""
cv2 es un módulo de Python que proporciona una interfaz para la biblioteca OpenCV 
(Open Source Computer Vision Library). OpenCV es una biblioteca de software de visión artificial y 
aprendizaje automático de código abierto que contiene una amplia colección de algoritmos de procesamiento 
de imágenes y visión por computadora. El módulo cv2 permite a los desarrolladores de Python acceder a muchas 
de las funciones y herramientas de OpenCV para procesar imágenes, realizar operaciones de visión por 
computadora, detección de objetos, seguimiento de objetos, reconocimiento de patrones y más.

PyAutoGUI es una biblioteca de Python que proporciona una interfaz simple para automatizar tareas repetitivas 
en un sistema operativo, como mover el mouse, hacer clic en elementos de la interfaz gráfica de usuario (GUI), 
escribir texto, realizar capturas de pantalla, entre otras funciones.
"""