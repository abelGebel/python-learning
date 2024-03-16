"""Ingresar repetidamente el legajo, nombre y las notas correspondientes al primer y 
segundo examen de un listado de alumnos. El ingreso de datos finaliza cuando se 
ingresa un legajo igual a cero. Calcular para cada alumno:
a. La nota final de cada alumno en base al promedio de las notas de los dos exámenes.
b. Mostrar el resultado de la cursada en base a lo siguiente:
- Nota Final entre [9 y 10]: SOBRESALIENTE
- Nota Final entre [7 y 9): DISTINGUIDO
- Nota Final entre (5 y 7): BUENO
- Nota Final entre [4 y 5]: SUFICIENTE
- Nota Final entre [0 y 4): INSUFICIENTE
Debe diseñar y luego reusar una función que permita cargar una nota válida 
(entre cero y diez)""" 
import os
import psycopg2
os.system('cls')
import tkinter as tk
from tkinter import messagebox

registroAlumnos = []

def ingresarAlumno():
    try:
        legajo = int(entry_A.get())
        nota1 = int(entry_C.get())
        nota2 = int(entry_D.get())
        if legajo==0:
            root.destroy()
        elif legajo < 0 :
            messagebox.showerror("Error", "Ingrese un valor válido.")
        elif (nota1 > 10 or nota1 < 1) or (nota2 > 10 or nota2 < 1):
            messagebox.showerror("Error", "Ingrese un valor válido.")
        else:
            nombre = str(entry_B.get())
            entry_A.delete(0, tk.END)  # Limpiar el campo de entrada
            entry_B.delete(0, tk.END) 
            entry_C.delete(0, tk.END)
            entry_D.delete(0, tk.END)

            promedio = float((nota1 + nota2)/2)
            resultado = ""
            if promedio < 4:
                resultado = "INSUFICIENTE"
            elif promedio >= 4 and promedio <= 5:
                resultado = "SUFICIENTE"
            elif promedio > 5 and promedio < 7:
                resultado = "BUENO"
            elif promedio >= 7 and promedio < 9:
                resultado = "DISTINGUIDO"
            else:
                resultado = "SOBRESALIENTE"

            cursor = connection.cursor()
            # Definir la consulta SQL para actualizar el registro en la tabla
            sql_insert = """INSERT INTO my_table (legajo, nombre, nota1, nota2, promedio, resultado) VALUES (%s, %s, %s, %s, %s, %s)"""
            # Ejecutar la consulta SQL con los valores proporcionados
            cursor.execute(sql_insert, (legajo, nombre, nota1, nota2, promedio, resultado))
            # Confirmar la transacción
            connection.commit()
            cursor.close()

    except:
        messagebox.showerror("Error", "Ingrese un valor válido.")

def mostrarNotas():
    os.system('cls')
    print("")
    print("LISTADO DE ALUMNOS")
    print("")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# principal-----------------------------------------------------
        
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'abel2023Fiunju123',
        database = 'my_database'
    )
except Exception as ex:
    print(ex)



root = tk.Tk()
root.title("Registro")

label_A = tk.Label(root, text=f"Legajo: ")
label_A.grid(row=0, column=0, padx=5, pady=5)

entry_A = tk.Entry(root)
entry_A.grid(row=0, column=1, padx=5, pady=5)

label_B = tk.Label(root, text=f"Nombre: ")
label_B.grid(row=1, column=0, padx=5, pady=5)

entry_B = tk.Entry(root)
entry_B.grid(row=1, column=1, padx=5, pady=5)

label_C = tk.Label(root, text=f"Nota 1er parcial: ")
label_C.grid(row=2, column=0, padx=5, pady=5)

entry_C = tk.Entry(root)
entry_C.grid(row=2, column=1, padx=5, pady=5)

label_D = tk.Label(root, text=f"Nota 2do parcial: ")
label_D.grid(row=3, column=0, padx=5, pady=5)

entry_D = tk.Entry(root)
entry_D.grid(row=3, column=1, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Ingresar", command=ingresarAlumno)
btn_promedio.grid(row=4, column=0, padx=5, pady=5)

btn_promedio = tk.Button(root, text="Mostrar listado", command=mostrarNotas)
btn_promedio.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()


connection.close()

