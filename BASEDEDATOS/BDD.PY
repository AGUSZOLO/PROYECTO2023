import mysql.connector
from faker import Faker

# Configuración de la base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Aberna_24$$",
    "database": "SALUDTEST333"
}

# Crear instancia de Faker
fake = Faker()

# Conexión a la base de datos
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

for _ in range(10):
    Nombre = fake.first_name()
    Contraseña = fake.word()
    Correo_elec = fake.email()
    Direccion = fake.word()
    Fecha_regis = fake.date_this_decade()

    insert_query = "INSERT INTO Usuario (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis) VALUES (%s, %s, %s, %s, %s)"
    insert_data = (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis)

    cursor.execute(insert_query, insert_data)
    connection.commit()


# Generar datos aleatorios para la tabla Carrito
for _ in range(10):
    Fecha_creacion = fake.date_this_decade()
    Estado = fake.word()

    Usuario_user_id = fake.random_int(min=1, max=10)

    insert_query = "INSERT INTO Carrito (Usuario_user_id, Fecha_creacion, Estado) VALUES (%s, %s, %s)"
    insert_data = (Usuario_user_id, Fecha_creacion, Estado)

    cursor.execute(insert_query, insert_data)
    connection.commit()

# Generar datos aleatorios para la tabla Producto
for _ in range(10):
    Nombre = fake.word()
    Precio = fake.random_int(min=10, max=1000)
    Descripcion = fake.word()
    Estado = fake.word()

    insert_query = "INSERT INTO Producto (Nombre, Precio, Descripcion, Estado) VALUES (%s, %s, %s, %s)"
    insert_data = (Nombre, Precio, Descripcion, Estado)

    cursor.execute(insert_query, insert_data)
    connection.commit()

# Generar datos aleatorios para la tabla Compra
for _ in range(10):
    Fecha_compra = fake.date_this_decade()
    Total = fake.random_int(min=10, max=1000)
    Cantidad  = fake.random_int(min=1, max=10)

    Usuario_user_id = fake.random_int(min=1, max=10)

    insert_query = "INSERT INTO Compra (Usuario_user_id, Fecha_compra, Total, Cantidad) VALUES (%s, %s, %s, %s)"
    insert_data = (Usuario_user_id, Fecha_compra, Total, Cantidad)

    cursor.execute(insert_query, insert_data)
    connection.commit()

for _ in range(10):
    Puntuacion= fake.random_int(min=1, max=5)
    Fecha = fake.date_this_decade()
    Usuario_user_id = fake.random_int(min=1, max=10)
    Producto_product_id = fake.random_int(min=1, max=10)

    insert_query ="INSERT INTO Valoracion (Puntuacion, Fecha, Usuario_user_id, Producto_product_id) VALUES (%s, %s, %s, %s)"
    insert_data = (Puntuacion, Fecha, Usuario_user_id, Producto_product_id)

    cursor.execute(insert_query, insert_data)
    connection.commit()


for _ in range(10):
    Puntuacion_comen= fake.random_int(min=1, max=10)
    Fecha_comen = fake.date_this_decade()
    Usuario_user_id = fake.random_int(min=1, max=10)
    Producto_product_id = fake.random_int(min=1, max=10)

    insert_query = "INSERT INTO Comentarios (Puntuacion_comen, Fecha_comen, Usuario_user_id, Producto_product_id) VALUES (%s, %s, %s, %s)"
    insert_data = (Puntuacion_comen, Fecha_comen, Usuario_user_id, Producto_product_id)

    cursor.execute(insert_query, insert_data)
    connection.commit()

print("Datos insertados correctamente.")


dry_run = False  # Cambia a True si deseas realizar una prueba

if dry_run:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        # Rollback para deshacer cambios en caso de prueba
        cnx.rollback()
    except mysql.connector.Error as exception:
        print(f"An error occurred during rollback:\n{exception}")
    finally:
        cursor.close()
        cnx.close()
else:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    try:
        # Confirmar cambios en caso de ejecución real
        cnx.commit()
    except mysql.connector.Error as exception:
        print(f"An error occurred during commit:\n{exception}")
    finally:
        cursor.close()
        cnx.close()