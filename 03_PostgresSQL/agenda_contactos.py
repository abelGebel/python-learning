''' Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de
teléfono. El programa debe mostrar el siguiente menú:

● Añadir/modificar: solicita un nombre, si el nombre se encuentra en la agenda, debe mostrar el teléfono
y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir
ingresar el teléfono correspondiente.

● Buscar: solicitando una cadena de caracteres, y muestra todos los contactos cuyos nombres empiezen 
por dicha cadena.

● Borrar: solicita un nombre y si existe nos preguntará si queremos borrarlo de la agenda. 

● Listar: muestra todos los contactos de la agenda.

Implementar el programa con una lista y una base de datos en postgresql.'''

import os
import psycopg2


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

def anadirModificar(connection):

    while True:

        nombre = verificarNombre()
        encontrado = False

        for i in range(len(agenda)):
            if agenda[i][0] == nombre:
                encontrado = True
                numero = agenda[i][1]
                posicion = i
                break

        if encontrado:
            print('El nombre ya se encuentra registrado con el numero:')
            print(numero)
            cambio = input('Desea cambiarlo?(s/n)')
            if cambio.lower() == 's':
                numero = verificarNumero()
                agenda[posicion][1] = numero

            # Crear un cursor
            cursor = connection.cursor()

            # Definir la consulta SQL para actualizar el registro en la tabla
            sql_update = """UPDATE contacto
                SET numero = %s
                WHERE nombre = %s"""

            # Valores para actualizar el registro
            nuevo_valor_columna1 = numero
            condicion = nombre

            # Ejecutar la consulta SQL con los valores proporcionados
            cursor.execute(sql_update, (nuevo_valor_columna1, condicion))

            # Confirmar la transacción
            connection.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()
                

        else:

            numero = verificarNumero()
            contacto = [nombre, numero]
            agenda.append(contacto)
            agenda.sort()

            # Crear un cursor
            cursor = connection.cursor()

            # Definir la consulta SQL para insertar un nuevo registro en la tabla
            sql_insert = """INSERT INTO contacto (nombre, numero)
            VALUES (%s, %s)"""

            # Valores para el nuevo registro
            valor_columna1 = nombre
            valor_columna2 = numero

            # Ejecutar la consulta SQL con los valores proporcionados
            cursor.execute(sql_insert, (valor_columna1, valor_columna2))

            # Confirmar la transacción
            connection.commit()

            # Cerrar el cursor
            cursor.close()

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


def borrar(agenda, connection):
    nombre = verificarNombre()
    
    encontrado = False

    for i in range(len(agenda)):
        if agenda[i][0] == nombre:
            encontrado = True
            numero = agenda[i][1]
            break    

    if encontrado:

        confirmar = input(f"Eliminar contacto {nombre}: {numero} ?(s/n) ")
        
        if confirmar.lower() == 's':

            agenda.remove([nombre, numero])


            cursor = connection.cursor()
            sql_update = """DELETE FROM contacto 
                WHERE nombre = %s"""


            # Ejecutar la consulta SQL con los valores proporcionados
            cursor.execute(sql_update, (nombre,))

            connection.commit()
            cursor.close()

    else:
        print("NOMBRE NO REGISTRADO")

    print('')
    continuar = input('(Presione ENTER para continuar)')
    os.system('cls')
    return agenda


def listar(agenda):
    print('---CONTACTOS---')
    print('')
    for contacto in agenda:
        print(f"{contacto[0]}: {contacto[1]}")
    print('')
    continuar = input('(Presione ENTER para continuar)')
    os.system('cls')


def cargar_datos(agenda, connection):
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contacto")
        rows = cursor.fetchall()
        for row in rows:
            registro = list(row)
            agenda.append(registro)

    except Exception as ex:
        print(ex)

    agenda.sort()
    return agenda


# Principal----------------------------------------------------------------------------------------
opcion = 0
agenda = []

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'abel2023Fiunju123',
        database = 'contacto_db'
    )
except Exception as ex:
    print(ex)


agenda = cargar_datos(agenda, connection)

while (True):
    opcion = menu()

    if opcion == 1:
        agenda = anadirModificar(connection)

    elif opcion == 2:
        buscar(agenda)

    elif opcion == 3:
        agenda = borrar(agenda, connection)

    elif opcion == 4:
        listar(agenda)

    elif opcion == 5:
        print('Fin registro')
        connection.close()
        break


