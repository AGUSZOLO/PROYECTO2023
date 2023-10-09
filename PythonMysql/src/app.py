import os
from webob import Request, Response
from jinja2 import Environment, FileSystemLoader
import database as db

template_path = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)

def home( environ, start_response):
    request = Request(environ)
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuario")
    result = cursor.fetchall()
    
    # Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in result:
        insertObject.append(dict(zip(columnNames, record)))
    
    cursor.close()
    
    response = render_template('index.html', data=insertObject)
    start_response('200 OK', [('Content-type', 'text/html')])
    return [response.encode('utf-8')]

#Añadir usuarios

def añadir(environ, start_response):
    request = Request(environ)
    
    if request.method == 'POST':
        form = request.POST
        Nombre = form.get('Nombre')
        Contraseña = form.get('Contraseña')
        Correo_elec = form.get('Correo_elec')
        Direccion = form.get('Direccion')
        Fecha_regis = form.get('Fecha_regis')

        if Nombre and Contraseña and Correo_elec and Direccion and Fecha_regis:
            cursor = db.database.cursor()
            sql = "INSERT INTO usuario (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis) VALUES (%s, %s, %s, %s, %s)"
            data = (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis)
            cursor.execute(sql, data)
            db.database.commit()
    
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [b'']

#Eliminar usuarios

def eliminar(environ, start_response):
    request = Request(environ)
    if request.method == 'GET':
        user_id = request.GET.get('id')
        if user_id:
            cursor = db.database.cursor()
            sql = "DELETE FROM usuario WHERE user_id=%s"
            data = (user_id,)
            cursor.execute(sql, data)
            db.database.commit()
    
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [b'']

#Editar usuarios

def editar(environ, start_response):
    request = Request(environ)
    
    if request.method == 'POST':
        form = request.POST
        Nombre = form.get('Nombre')
        Contraseña = form.get('Contraseña')
        Correo_elec = form.get('Correo_elec')
        Direccion = form.get('Direccion')
        Fecha_regis = form.get('Fecha_regis')
        user_id = form.get('user_id')

        if Nombre and Contraseña and Correo_elec and Direccion and Fecha_regis and user_id:
            cursor = db.database.cursor()
            sql = "UPDATE usuario SET Nombre= %s, Contraseña=%s, Correo_elec=%s, Direccion=%s, Fecha_regis=%s WHERE user_id=%s"
            data = (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis, user_id)
            cursor.execute(sql, data)
            db.database.commit()
    
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [b'']

def render_template(template_name, **context):
    t = jinja_env.get_template(template_name)
    return t.render(context)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 4000, home)
    print("Servidor en ejecución en http://localhost:4000/")
    httpd.serve_forever()