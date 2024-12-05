from flask import Flask, render_template, request, redirect, flash

import controlador_juegos

app = Flask(__name__)

@app.route("/")
@app.route("/juego")
def juego():
    juegos = controlador_juegos.obtener_juegos()
    return render_template("juego.html",juegos=juegos)

@app.route('/agregar_juego')
def formulario_agregar_juego():
    return render_template("agregar_juego.html")





@app.route("/guardar_juego", methods=["POST"])
def guardar_juego():
    
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    
    
    controlador_juegos.insertar_juego(nombre, descripcion, precio)
    
    return redirect("/juego")

# Ruta: eliminar_juego
@app.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    controlador_juegos.eliminar_juego(request.form["id"])
    return redirect("/juego")

@app.route("/formulario_detalle_juego/<int:id>")
def detalle_juego(id):
    # Obtener el juego por ID
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("detalle_juego.html", juego=juego)

# Ruta: formulario_editar_juego
@app.route("/formulario_editar_juego/<int:id>")
def editar_juego(id):
    # Obtener el juego por ID
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)

# Ruta: actualizar_juego
@app.route("/actualizar_juego", methods=["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_juegos.actualizar_juego(nombre, descripcion, precio, id)
    return redirect("/juego")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
    

    