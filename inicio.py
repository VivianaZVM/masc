from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
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

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
    cursor = conn.cursor()
    cursor.execute('select id, usuario, contraseña from usuarios where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        corr=request.form['usuario']
        come=request.form['contraseña']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
        cursor = conn.cursor()
        cursor.execute('update usuarios set usuario=%s, contraseña=%s where id=%s', (corr,come,id))
        conn.commit()
    return redirect(url_for('Servicios'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
    cursor = conn.cursor()
    cursor.execute('delete from usuarios where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('Servicios'))

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")

@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
    cursor = conn.cursor()
    cursor.execute('select id, usuario, contraseña from usuarios order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", comentarios = datos)

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_usuario = request.form['usuario']
        aux_contraseña = request.form['contraseña']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='solicitud_registro')
        cursor = conn.cursor()
        cursor.execute('insert into usuarios (usuario,contraseña) values (%s, %s)',(aux_usuario, aux_contraseña))
        conn.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)