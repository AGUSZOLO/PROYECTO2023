from db import get_conn_n_cursor
from wsgi_app import Wsgiclass, render_template

app = Wsgiclass()


@app.ruta("/")
def home_page(request, response):
    html_respuesta = render_template("home.html")
    response.text = html_respuesta["text"]
    response.content_type = html_respuesta["type"]


@app.ruta("/usuarios")
def home_page(request, response):
    cnx, curs = get_conn_n_cursor(dictionary=True)
    curs.execute("SELECT * FROM usuario")
    data = curs.fetchall()

    html_respuesta = render_template("tabla-generica.html", data=data)
    response.text = html_respuesta["text"]
    response.content_type = html_respuesta["type"]
