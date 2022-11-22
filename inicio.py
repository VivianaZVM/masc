import pymysql
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/NuestraEmpresa')
def NuestraEmpresa():
    return render_template("NuestraEmpresa.html")

@app.route('/Servicios')
def Servicios():
    return render_template("Servicios.html")

@app.route('/Contactos')
def Contactos():
    return render_template("Contactos.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")

@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
    cursor = conn.cursor()
    cursor.execute('select id, Nombre, Correo, Telefono, Direccion, Ocacion from usuarios order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", comentar = datos)

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Nombre = request.form['Nombre']
        aux_Correo = request.form['Correo']
        aux_Telefono = request.form['Telefono']
        aux_Direccion = request.form['Direccion']
        aux_Ocacion = request.form['Ocacion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
        cursor = conn.cursor()
        cursor.execute('insert into usuarios (Nombre,Correo,Telefono,Direccion,Ocacion) values (%s, %s, %s, %s, %s)',(aux_Nombre, aux_Correo, aux_Telefono, aux_Direccion, aux_Ocacion))
        conn.commit()
    return redirect(url_for('index'))

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
    cursor = conn.cursor()
    cursor.execute('select id, Nombre, Correo, Telefono, Direccion, Ocacion from usuarios where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        aux_Nombre = request.form['Nombre']
        aux_Correo = request.form['Correo']
        aux_Telefono = request.form['Telefono']
        aux_Direccion = request.form['Direccion']
        aux_Ocacion = request.form['Ocacion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
        cursor = conn.cursor()
        cursor.execute('UPDATE usuarios set Nombre=%s, Correo=%s, Telefono=%s, Direccion=%s, Ocacion=%s where id=%s', (aux_Nombre, aux_Correo, aux_Telefono, aux_Direccion, aux_Ocacion,id))
        conn.commit()
    return redirect(url_for('crud'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
    cursor = conn.cursor()
    cursor.execute('delete from usuarios where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))



@app.route('/carrito')
def carrito():
    return render_template("carrito.html")

if __name__ == "__main__":
    app.run(debug=True)