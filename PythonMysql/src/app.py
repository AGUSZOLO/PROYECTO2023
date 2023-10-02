from flask import Flask, render_template, request, redirect, url_for
import os  
import database as db 

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src','templates')

app = Flask(__name__, template_folder = template_dir)


#rutas de la aplicacion

@app.route('/')
def home(): 
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuario")
    result = cursor.fetchall()
    #convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in  cursor.description]
    for record in result:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html',data=insertObject)


#ruta para guardar usuarios en la bdd
@app.route('/usuario',methods=['post'])
def añadir():
    Nombre = request.form['Nombre']
    Contraseña = request.form['Contraseña']
    Correo_elec = request.form['Correo_elec']
    Direccion = request.form['Direccion']
    Fecha_regis = request.form['Fecha_regis']

    if Nombre and Contraseña and Correo_elec and Direccion and Fecha_regis:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuario (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis) VALUES (%s, %s, %s, %s, %s)"
        data= (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


@app.route('/eliminar/<string:id>')
def eliminar(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuario WHERE user_id=%s"
    data= (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))


@app.route('/editar/<string:id>', methods=['post'])
def editar(id):
    Nombre = request.form['Nombre']
    Contraseña = request.form['Contraseña']
    Correo_elec = request.form['Correo_elec']
    Direccion = request.form['Direccion']
    Fecha_regis = request.form['Fecha_regis']

    if Nombre and Contraseña and Correo_elec and Direccion and Fecha_regis:
        cursor = db.database.cursor()
        sql = "UPDATE usuario SET Nombre= %s, Contraseña=%s, Correo_elec=%s, Direccion=%s, Fecha_regis=%s WHERE user_id=%s"
        data= (Nombre, Contraseña, Correo_elec, Direccion, Fecha_regis, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)