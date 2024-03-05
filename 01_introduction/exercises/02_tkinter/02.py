"""Diseñe un programa que permita calcular el cuadrado, el cubo y la cuarta 
potencia de un número ingresado por el usuario."""
import os
os.system('cls')

import tkinter as tk
from tkinter import messagebox

def elevar(exponente):
    
    try:
        valor = (float(entry_A.get()))**exponente
        messagebox.showinfo("",f"Resultado: {valor}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Calculadora")

"""
# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana en la pantalla
x = (screen_width - 400) // 2  # Ancho de la ventana
y = (screen_height - 300) // 2  # Altura de la ventana

# Establecer la geometría de la ventana
root.geometry(f"400x300+{x}+{y}")
"""

label_A = tk.Label(root, text="Numero:")
label_A.grid(row=0, column=0, padx=5, pady=5)

entry_A = tk.Entry(root)
entry_A.grid(row=1, column=0, padx=5, pady=5)

btn_raiz = tk.Button(root, text="Elevar al cuadado", command=lambda: elevar(2), height=2)
btn_raiz.grid(row=2, column=0, padx=5, pady=5)

btn_raiz = tk.Button(root, text="Elevar al cubo", command=lambda: elevar(3), height=2)
btn_raiz.grid(row=3, column=0, padx=5, pady=5)

btn_raiz = tk.Button(root, text="Elevar a la cuarta potencia", command=lambda: elevar(4), height=2)
btn_raiz.grid(row=4, column=0, padx=5, pady=5)

btn_raiz = tk.Button(root, text="Salir", command=salir, width=10, height=2)
btn_raiz.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
