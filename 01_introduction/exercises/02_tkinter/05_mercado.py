"""Diseñe un algoritmo que permita calcular la venta de productos hasta que 
el operador no quiera continuar. Por cada uno de ellos se ingresa el precio, 
el número de unidades a comprar, y se calcula el importe. Considere además que 
a partir de 5 unidades se realiza un descuento del 10% sobre el total de la compra.
Al finalizar del ingreso de productos debe mostrar el total a pagar por el cliente."""

import os
os.system('cls')
import tkinter as tk
from tkinter import messagebox

productos = []

def ingresarProducto():
    try:
        precio = float(entry_A.get())
        cantidad = float(entry_B.get())
        entry_A.delete(0, tk.END)  # Limpiar el campo de entrada
        entry_B.delete(0, tk.END)  # Limpiar el campo de entrada
        if cantidad >= 5:
            subtotal = (precio*cantidad)*0.90
        subtotal = (precio*cantidad)
        productos.append(subtotal)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor válido.")

def calcularTotal():
    if productos:
        total = sum(productos)
        messagebox.showinfo("", f"Total a pagar: {total:.2f}")
    else:
        messagebox.showinfo("No se han ingresado productos.")

def limpiarRegistro():
    productos.clear()

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

entry_B = tk.Entry(root)
entry_B.grid(row=1, column=1, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Ingresar valor", command=ingresarProducto)
btn_promedio.grid(row=2, column=0, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Calcular total", command=calcularTotal)
btn_promedio.grid(row=2, column=1, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Limpiar registro", command=limpiarRegistro)
btn_promedio.grid(row=3, column=0, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Salir", command=salir)
btn_promedio.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()
