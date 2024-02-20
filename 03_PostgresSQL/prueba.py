import os
os.system('cls')

agenda = [
    (34, 'Maxi'),
    (98, 'Sergio'),
    (22, 'Daniel'),
    (83, 'Abel')
]

agenda.pop(0)
print(agenda)

# Bandera para indicar si se encontró el nombre
encontrado = False
nombre_buscado = 'Abel'
# Itera sobre cada tupla en la lista
for numero, nombre in agenda:
    if nombre == nombre_buscado:
        encontrado = True
        break

# Verifica si se encontró el nombre
if encontrado:
    print(f"El nombre '{nombre_buscado}' está en la lista.")
else:
    print(f"El nombre '{nombre_buscado}' no está en la lista.")

print(agenda[2][1])

string = "A"

print(string.lower())

tup = (34, 'Maxi')


tup = list(tup)

print(type(tup))

