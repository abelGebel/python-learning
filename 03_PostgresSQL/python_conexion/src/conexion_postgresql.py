import psycopg2

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = 'abel2023Fiunju123',
        database = 'curso_db'
    )
    print("Conexion exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)

    cursor.execute("SELECT * FROM alumno")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")

