from flask import Flask
from flask import render_template, request
from flask import redirect
from flask import url_for

import psycopg2 as pg2



app = Flask(__name__)


          # -------------------------------------------- PAGINAS PRODUCTO ---------------------------------------------------- #

@app.route('/comprar_camisa1')
def comprar_camisa1():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 1')
    camiseta1 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto.html',camiseta1 = camiseta1)

@app.route('/comprar_camisa2')
def comprar_camisa2():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 2')
    camiseta2 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto2.html',camiseta2 = camiseta2)

@app.route('/comprar_camisa3')
def comprar_camisa3():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 3')
    camiseta3 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto3.html', camiseta3 = camiseta3)

@app.route('/comprar_camisa4')
def comprar_camisa4():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 4')
    camiseta4 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto4.html', camiseta4 = camiseta4)

@app.route('/comprar_camisa5')
def comprar_camisa5():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 5')
    camiseta5 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto5.html',camiseta5 = camiseta5)

@app.route('/comprar_camisa6')
def comprar_camisa6():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 6')
    camiseta6 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto6.html', camiseta6 = camiseta6)

@app.route('/comprar_camisa7')
def comprar_camisa7():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 7')
    camiseta7 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto7.html', camiseta7 = camiseta7)

@app.route('/comprar_camisa8')
def comprar_camisa8():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 8')
    camiseta8 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto8.html', camiseta8 = camiseta8)

@app.route('/comprar_camisa9')
def comprar_camisa9():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 9')
    camiseta9 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto9.html', camiseta9 = camiseta9)

@app.route('/comprar_camisa10')
def comprar_camisa10():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 10')
    camiseta10 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto10.html', camiseta10 = camiseta10)

@app.route('/comprar_camisa11')
def comprar_camisa11():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 11')
    camiseta11 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto11.html', camiseta11 = camiseta11)

@app.route('/comprar_camisa12')
def comprar_camisa12():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 12')
    camiseta12 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto12.html', camiseta12 = camiseta12)

@app.route('/comprar_camisa13')
def comprar_camisa13():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 13')
    camiseta13 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto13.html', camiseta13 = camiseta13)

@app.route('/comprar_camisa14')
def comprar_camisa14():
        
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE id_producto = 14')
    camiseta14 = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    return render_template('camisetas/producto14.html', camiseta14 = camiseta14)

              # ------------------------------------------------------------------------------------------------------------ #



        # -------------------------------------------- PAGINA INICIO SESION ---------------------------------------------------- #
        
        
@app.route('/')
def home():
    
    return render_template('index.html')
        
        
        
        
        
        
        
        
        
        

            # ------------------------------------------------------------------------------------------------------------ #



           # -------------------------------------------- PAGINA NOSOTROS ---------------------------------------------------- #

@app.route('/pagina_nosotros')
def pagina_nosotros():
    return render_template('nosotros.html')

              # ------------------------------------------------------------------------------------------------------------ #
              
              
              # -------------------------------------------- ALMACEN ---------------------------------------------------- #
              
              
@app.route('/almacen')
def almacen():
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" ORDER BY id_producto')
    productos = cursor.fetchall()
    
    conexion.commit()
    return render_template('almacen/almacen.html',productos = productos)

@app.route('/crearCamiseta')
def crearCamiseta():
    
    return render_template('almacen/crearCamiseta.html')
           
           
@app.route('/almacenarCamiseta', methods=['POST'])
def almacenarCamiseta():
    _nombre = request.form['txtNombre']
    _precio = request.form['txtPrecio']
    _stock = request.form['txtStock']
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    sql = 'INSERT INTO "public"."Productos" (nombre,precio,stock) VALUES (%s, %s, %s)'
    parametros = (_nombre, _precio, _stock)
    cursor.execute(sql,parametros)
    conexion.commit()
    conexion.close()
    
    return redirect(url_for('almacen'))


@app.route('/eliminarCamiseta/<int:id>')
def eliminar(id):
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM "public"."Productos" WHERE "Productos".id_producto = %s',(id,))
              
    conexion.commit()
    conexion.close()
    
    return redirect(url_for('almacen'))


@app.route('/modificarCamiseta/<int:id>')
def modificarCamiseta(id):
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM "public"."Productos" WHERE "Productos".id_producto=%s', (id,))
    producto = cursor.fetchall()
    conexion.commit()
    
    return render_template('almacen/editarCamiseta.html', producto = producto)


@app.route('/actualizarCamiseta', methods=['POST'])
def actualizarCamiseta():
    _nombre = request.form['txtNombre']
    _precio = request.form['txtPrecio']
    _stock = request.form['txtStock']
    id = request.form['txtID']
    
    
    conexion = pg2.connect(database = 'Web_venta_camisetas', user = 'postgres', password = 'Xispita18.')
    cursor = conexion.cursor()
    
    sql = '''UPDATE "public"."Productos" 
             SET nombre = %s, precio = %s, stock = %s 
             WHERE id_producto = %s'''
    parametros = (_nombre, _precio, _stock,id)
    cursor.execute(sql,parametros)
    conexion.commit()
    conexion.close()
    return redirect(url_for('almacen'))

              # ---------------------------------------------------------------------------------- #

@app.route('/pagina_tienda')
def pagina_tienda():
    return render_template('index.html')

@app.route('/retornar_inicio', methods=['GET', 'POST'])
def retornar_inicio():
    return redirect(url_for('home'))

@app.route('/pagina_principal')
def pagina_principal():
    
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    