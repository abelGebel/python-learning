from tkinter import *
from tkinter import ttk
root = Tk() #crear la instancia de la clase Tk
frm = ttk.Frame(root, padding=20) #se crea el marco del widget, el cual en este caso contendrá la etiqueta y el botón que crearemos después.
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()#muestra todo en pantalla y responde a la entrada del usuario hasta que el programa termina.


"""widgets
Una interfaz de usuario de Tkinter está compuesta de varios widgets individuales. 
Cada widget es representado como un objeto de Python, instanciado desde clases tales como ttk.Frame, 
ttk.Label y ttk.Button."""

