"""Diseñe un algoritmo que permita calcular las mediciones de temperaturas de 
una caldera, las mismas solo pueden ser mayores a 20 grados, si se ingresan valores 
inferiores a estos se debe volver a pedir el valor.
Al final del proceso mostrar el promedio de todos los valores ingresados."""

import os
os.system('cls')
import tkinter as tk
from tkinter import messagebox

# Lista para almacenar las temperaturas ingresadas
temperaturas = []

def agregarTemperatura(event):
    try:
        temperatura = float(entry_A.get())
        if temperatura > 20:
            temperaturas.append(temperatura)
            entry_A.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "La temperatura debe ser mayor a 20 grados.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido para la temperatura.")

def ingresarTemperatura():
    try:
        temperatura = float(entry_A.get())
        if temperatura > 20:
            temperaturas.append(temperatura)
            entry_A.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "La temperatura debe ser mayor a 20 grados.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido para la temperatura.")

def mostrarPromedio():
    if temperaturas:
        promedio = sum(temperaturas) / len(temperaturas)
        messagebox.showinfo("Promedio de temperaturas", f"El promedio de las temperaturas ingresadas es: {promedio:.2f}")
    else:
        messagebox.showinfo("Promedio de temperaturas", "No se han ingresado temperaturas.")

def reiniciarAcumulador():
    temperaturas.clear()


def salir():
    root.destroy()

root = tk.Tk()
root.title("Temperaturas")

label_A = tk.Label(root, text="Temperatura registrada:")
label_A.grid(row=0, column=0, padx=5, pady=5)

entry_A = tk.Entry(root)
entry_A.grid(row=0, column=1, padx=5, pady=5)

# Llamar a la función agregarTemperatura cuando se presiona Enter en el campo de entrada
entry_A.bind("<Return>", agregarTemperatura)

btn_promedio = tk.Button(root, text="Mostrar promedio", command=mostrarPromedio)
btn_promedio.grid(row=1, column=0, columnspan=1, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Ingresar valor", command=ingresarTemperatura)
btn_promedio.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Reiniciar acumulador", command=reiniciarAcumulador)
btn_promedio.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Salir", command=salir)
btn_promedio.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
