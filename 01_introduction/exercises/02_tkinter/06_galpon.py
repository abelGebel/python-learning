"""Un galpón tiene al comienzo de la jornada una cantidad inicial (Stock inicial) de 
cajones con productos de un solo tipo, luego repetidamente, entran y salen camiones, 
que traen o llevan cantidades de cajones. Si no alcanza la cantidad a llevar, se 
debe mostrar un mensaje “NO ALCANZA”, se lleva todo lo que hay; se muestra lo que
se lleva y el galpón queda vacío. Se muestra al final de la jornada cuantos cajones 
hay en el galpón (Stock final), y cuantos cajones ingresaron y cuantos cajones 
salieron en toda la jornada."""
import os
os.system('cls')
import tkinter as tk
from tkinter import messagebox

stock = 1000
ingresado = 0
retirado = 0

def ingresar():
    try:
        global stock, ingresado
        cantidadAIngresar = int(entry_A.get())
        stock += cantidadAIngresar
        ingresado += cantidadAIngresar
        entry_A.delete(0, tk.END)  # Limpiar el campo de entrada
        label_A.config(text=f"Cantidad de cajones: {stock}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor válido.")




def retirar():
    global stock, retirado
    cantidadALlevar = int(entry_A.get())
    if cantidadALlevar > stock:
        messagebox.showinfo("", f"NO ALCNAZA: retira {stock}")
        entry_A.delete(0, tk.END)  # Limpiar el campo de entrada
        retirado += stock
        stock = 0
    else:
        stock -= cantidadALlevar
        retirado += cantidadALlevar
        entry_A.delete(0, tk.END)  # Limpiar el campo de entrada

    label_A.config(text=f"Cantidad de cajones: {stock}")


def salir():
    messagebox.showinfo("Informacion",f"Stock final: {stock}.\nIngresaron: {ingresado}\nSalieron: {retirado}")
    root.destroy()

root = tk.Tk()
root.title("Ventas")

label_A = tk.Label(root, text=f"Cantidad de cajones: {stock}")
label_A.grid(row=0, column=0, padx=5, pady=5)

entry_A = tk.Entry(root)
entry_A.grid(row=1, column=0, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Ingresar", command=ingresar)
btn_promedio.grid(row=1, column=1, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Retirar", command=retirar)
btn_promedio.grid(row=1, column=2, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Salir", command=salir)
btn_promedio.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

root.mainloop()
