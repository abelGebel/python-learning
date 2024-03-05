"""Diseñe un algoritmo que determine si un número es positivo, negativo o cero, 
el proceso finaliza cuando el operador no desea continuar."""
import os
os.system('cls')
import tkinter as tk
from tkinter import messagebox

def clasificarNumero(num):
    try:
        num = int(num)
        if num > 0:
            result_label.config(text="El número es positivo.")
        elif num < 0:
            result_label.config(text="El número es negativo.")
        else:
            result_label.config(text="El número es cero.")
    except:
        result_label.config(text="Ingrese valores enteros válidos.")


def salir():
    root.destroy()

root = tk.Tk()
root.title("Clasificar numero")

label_A = tk.Label(root, text="Numero:")
label_A.grid(row=0, column=0, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, padx=5, pady=5)

entry_A = tk.Entry(root)
entry_A.grid(row=1, column=0, padx=5, pady=5)

btn_raiz = tk.Button(root, text="Clasificar numero", command=lambda: clasificarNumero(entry_A.get()))
btn_raiz.grid(row=2, column=0, padx=5, pady=5)

btn_salir = tk.Button(root, text="Salir", command=salir)
btn_salir.grid(row=5, column=0, padx=5, pady=5)


# Cerrar la ventana emergente al hacer clic fuera de ella
def cerrarVentanaEmergente(event):
    result_label.config(text="")
root.bind("<Button-1>", cerrarVentanaEmergente)

root.mainloop()
