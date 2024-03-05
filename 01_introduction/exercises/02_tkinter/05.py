"""Diseñe un algoritmo que permita calcular la venta de productos hasta que 
el operador no quiera continuar. Por cada uno de ellos se ingresa el precio, 
el número de unidades a comprar, y se calcula el importe. Considere además que 
a partir de 5 unidades se realiza un descuento del 10% sobre el total de la compra.
Al finalizar del ingreso de productos debe mostrar el total a pagar por el cliente."""

import os
os.system('cls')
import tkinter as tk
from tkinter import messagebox


def salir():
    root.destroy()

root = tk.Tk()
root.title("Ventas")

label_A = tk.Label(root, text="Precio:")
label_A.grid(row=0, column=0, padx=5, pady=5)

entry_A = tk.Entry(root)
entry_A.grid(row=0, column=1, padx=5, pady=5)

label_A = tk.Label(root, text="Cantidad:")
label_A.grid(row=1, column=0, padx=5, pady=5)

entry_A = tk.Entry(root)
entry_A.grid(row=1, column=1, padx=5, pady=5)





root.mainloop()
