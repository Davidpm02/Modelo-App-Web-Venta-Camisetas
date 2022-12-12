from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for



app = Flask(__name__)



          # -------------------------------------------- PAGINAS PRODUCTO ---------------------------------------------------- #

@app.route('/comprar_camisa1')
def comprar_camisa1():
    return render_template('producto.html')

@app.route('/comprar_camisa2')
def comprar_camisa2():
    return render_template('producto2.html')

@app.route('/comprar_camisa3')
def comprar_camisa3():
    return render_template('producto3.html')

@app.route('/comprar_camisa4')
def comprar_camisa4():
    return render_template('producto4.html')

@app.route('/comprar_camisa5')
def comprar_camisa5():
    return render_template('producto5.html')

@app.route('/comprar_camisa6')
def comprar_camisa6():
    return render_template('producto6.html')

@app.route('/comprar_camisa7')
def comprar_camisa7():
    return render_template('producto7.html')

@app.route('/comprar_camisa8')
def comprar_camisa8():
    return render_template('producto8.html')

@app.route('/comprar_camisa9')
def comprar_camisa9():
    return render_template('producto9.html')

@app.route('/comprar_camisa10')
def comprar_camisa10():
    return render_template('producto10.html')

@app.route('/comprar_camisa11')
def comprar_camisa11():
    return render_template('producto11.html')

@app.route('/comprar_camisa12')
def comprar_camisa12():
    return render_template('producto12.html')

@app.route('/comprar_camisa13')
def comprar_camisa13():
    return render_template('producto13.html')

@app.route('/comprar_camisa14')
def comprar_camisa14():
    return render_template('producto14.html')

              # ------------------------------------------------------------------------------------------------------------ #








           # -------------------------------------------- PAGINA NOSOTROS ---------------------------------------------------- #

@app.route('/pagina_nosotros')
def pagina_nosotros():
    return render_template('nosotros.html')

              # ------------------------------------------------------------------------------------------------------------ #
              
              
              
              
              

@app.route('/pagina_tienda')
def pagina_tienda():
    return render_template('index.html')

@app.route('/retornar_inicio', methods=['GET', 'POST'])
def retornar_inicio():
    return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    