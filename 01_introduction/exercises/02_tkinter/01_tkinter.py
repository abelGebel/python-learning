import tkinter as tk
from tkinter import messagebox
import math
import os
os.system('cls')

def calcular_raiz():
    try:
        valor_A = float(entry_A.get())
        raiz = math.sqrt(valor_A)
        messagebox.showinfo("Resultado", f"La raíz cuadrada de {valor_A} es {round(raiz, 2)}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido para A.")

def calcular_producto():
    try:
        valor_A = float(entry_A.get())
        valor_B = float(entry_B.get())
        producto = valor_A * valor_B
        messagebox.showinfo("Resultado", f"El producto de {valor_A} y {valor_B} es {round(producto, 2)}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para A y B.")

def calcular_cociente():
    try:
        valor_A = float(entry_A.get())
        valor_B = float(entry_B.get())
        cociente = valor_A / valor_B
        messagebox.showinfo("Resultado", f"El cociente entre {valor_A} y {valor_B} es {round(cociente, 2)}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para A y B.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero.")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Calculadora")

label_A = tk.Label(root, text="Valor de A:")
label_A.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_A = tk.Entry(root)
entry_A.grid(row=0, column=1, padx=5, pady=5)

label_B = tk.Label(root, text="Valor de B:")
label_B.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_B = tk.Entry(root)
entry_B.grid(row=1, column=1, padx=5, pady=5)



btn_raiz = tk.Button(root, text="Calcular raíz", command=calcular_raiz)
btn_raiz.grid(row=2, column=0, padx=5, pady=5)

btn_producto = tk.Button(root, text="Calcular producto", command=calcular_producto)
btn_producto.grid(row=2, column=1, padx=5, pady=5)

btn_cociente = tk.Button(root, text="Calcular cociente", command=calcular_cociente)
btn_cociente.grid(row=3, column=0, padx=5, pady=5)

btn_salir = tk.Button(root, text="Salir", command=salir)
btn_salir.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
