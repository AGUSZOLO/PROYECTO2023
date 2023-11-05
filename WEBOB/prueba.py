from db import get_conn_n_cursor
import config as db
from wsgi_app import Wsgiclass, render_template
from waitress import serve

app = Wsgiclass()

@app.ruta("/")
def home(request, response):
    cnx, curs = get_conn_n_cursor(dictionary=True)
    curs.execute("SELECT * FROM usuario")
    data = curs.fetchall()

    response.content_type = render_template("index.html", data=data)["type"]
    response.text = render_template("index.html", data=data)["text"]

# Añadir usuarios
@app.ruta("/añadir")
def añadir(request, response):
    if request.method == 'POST':
        form = request.POST
        Nombre = form.get('Nombre')
        Contraseña = form.get('Contraseña')
        Correo_elec = form.get('Correo_elec')
        Direccion = form.get('Direccion')
        Fecha_regis = form.get('Fecha_regis')

        if Nombre and Contraseña and Correo_elec and Direccion and Fecha_regis:
            cursor = db.DB_CONFIG.cursor()
            sql = "INSERT INTO usuario (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis) VALUES (%s, %s, %s, %s, %s)"
            data = (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis)
            cursor.execute(sql, data)
            db.DB_CONFIG.commit()

    response.status_code = 200
    response.headers['Content-type'] = 'text/html'
    return response

# Eliminar usuarios
@app.ruta("/eliminar")
def eliminar(request, response):
    user_id = request.GET.get('id')
    if user_id:
        cursor = db.DB_CONFIG.cursor()
        sql = "DELETE FROM usuario WHERE user_id=%s"
        data = (user_id,)
        cursor.execute(sql, data)
        db.DB_CONFIG.commit()

    response.status_code = 200
    response.headers['Content-type'] = 'text/html'
    return response

# Editar usuarios
@app.ruta("/editar")
def editar(request, response):
    if request.method == 'POST':
        form = request.POST
        Nombre = form.get('Nombre')
        Contraseña = form.get('Contraseña')
        Correo_elec = form.get('Correo_elec')
        Direccion = form.get('Direccion')
        Fecha_regis = form.get('Fecha_regis')
        user_id = form.get('user_id')

        if Nombre and Contraseña and Correo_elec and Direccion and Fecha_regis and user_id:
            cursor = db.d.cursor()
            sql = "UPDATE usuario SET Nombre= %s, Contraseña=%s, Correo_elec=%s, Direccion=%s, Fecha_regis=%s WHERE user_id=%s"
            data = (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis, user_id)
            cursor.execute(sql, data)
            db.DB_CONFIG.commit()

    response.status_code = 200
    response.headers['Content-type'] = 'text/html'
    return response