''' Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de
teléfono. El programa debe mostrar el siguiente menú:

● Añadir/modificar: solicita un nombre, si el nombre se encuentra en la agenda, debe mostrar el teléfono
y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir
ingresar el teléfono correspondiente.

● Buscar: solicitando una cadena de caracteres, y muestra todos los contactos cuyos nombres empiezen 
por dicha cadena.

● Borrar: solicita un nombre y si existe nos preguntará si queremos borrarlo de la agenda. Si existe más de
uno debe identificarlos por un número secuencial que permita al usuario identificarlo para realizar la
operación de borrado 

● Listar: muestra todos los contactos de la agenda.
Implementar el programa con una lista.'''

import os


def verificarOpcion():
    while (True):
        try:
            op = int(input("Ingrese una opcion: "))
            if 1 <= op <= 5:
                break
            else:
                print("INGRESO NO VALIDO...")
        except:
            print("INGRESO NO VALIDO...")
    return op

def menu():
    print('--------AGENDA--------')
    print("1) Añadir/modificar. ")
    print("2) Buscar.")
    print("3) Borrar.")
    print("4) Listar.")
    print('5) Salir.')
    opcion = verificarOpcion()
    os.system('cls')
    return opcion

def verificarNombre():
    while True:
        nombre = input('Nombre: ')
        if nombre == '' or nombre.replace(' ', '').isalpha() == False:
            print('INGRESO NO VALIDO...')
        else:
            return nombre

def verificarNumero():
    while True:
        numero = input('Numero: ')
        if numero.isnumeric() == False:
            print('INGRESO NO VALIDO...')
        else:
            return str(numero)

def anadirModificar():

    while True:

        nombre = verificarNombre()

        encontrado = False

        for i in range(len(agenda)):
            if agenda[i][1] == nombre:
                encontrado = True
                numero = agenda[i][0]
                posicion = i
                break


        if encontrado:
            print('El nombre ya se encuentra registrado con el numero:')
            print(numero)
            cambio = input('Desea cambiarlo?(s/n)')
            if cambio.lower() == 's':
                numero = verificarNumero()
                agenda[posicion][0] = numero
        else:
            numero = verificarNumero()
            contacto = [numero, nombre]
            agenda.append(contacto)
            print('Contacto agregado correctamente.')
        print('')
        continuar = input('Desea continuar?(s/n)')
        os.system('cls')
        if continuar.lower() == 'n':
            break

    return agenda


def buscar(agenda):
    cadena = input('Ingrese una busqueda: ')
    for contacto in agenda:
        if contacto[1].lower().startswith(cadena.lower()):
            print(f"{contacto[1]}: {contacto[0]}")
    print('')
    continuar = input('(Presione ENTER para continuar)')
    os.system('cls')


def borrar(agenda):
    nombre = verificarNombre()
    lista_aux = []
    cont = 0

    for i in range(len(agenda)):
        if agenda[i][1] == nombre:
            lista_aux.append([agenda[i], i])
            cont += 1
            

    if cont == 0:
        print("Nombre no registrado.")

    elif cont == 1:

        continuar = input(f'Desea eliminar el contacto {lista_aux[0][0]}? (s/n) ')
        if(continuar.lower() == "s"):
            agenda.pop(lista_aux[0][1])

    else:

        for i in range (len(lista_aux)):
            print(f"{i}: {lista_aux[i][0]}")
        contacto_borrar = input("Cual de estos contactos desea borrar? ")

        for i in range (len(lista_aux)):
            if int(contacto_borrar) == i:
                agenda.pop(lista_aux[i][1])
                break

    print('')
    continuar = input('(Presione ENTER para continuar)')
    os.system('cls')
    return agenda


def listar(agenda):
    print('---CONTACTOS---')
    print('')
    for contacto in agenda:
        print(f"{contacto[1]}: {contacto[0]}")
    print('')
    continuar = input('(Presione ENTER para continuar)')
    os.system('cls')




# Principal----------------------------------------------------------------------------------------
os.system('cls')
opcion = 0
agenda = [
    ['34', 'm'],
    ['30', 'm'],
    ['98', 'Sergio'],
    ['22', 'Daniel'],
    ['83', 'Abel'],
    ['91', 'Marcelo']
]

while (True):
    opcion = menu()

    if opcion == 1:
        agenda = anadirModificar()

    elif opcion == 2:
        buscar(agenda)

    elif opcion == 3:
        agenda = borrar(agenda)

    elif opcion == 4:
        listar(agenda)

    elif opcion == 5:
        print('Fin registro')
        break


