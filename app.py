from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return render_template('home.html')

# Página de cálculo ACI (ya existente)
@app.route('/aci')
def aci():
    return render_template('index.html')

# Página de Geotecnia – Muros
@app.route('/geotecnia')
def geotecnia():
    return render_template('muros.html')

# Ruta de cálculo (ya la tenés armada con tu lógica actual)
@app.route('/calcular', methods=['POST'])
def calcular():
    # Acá mantené la lógica que ya tenías para calcular cemento, arena, etc.
    # Ejemplo base:
    volumen = float(request.form['volumen'])
    peso_bulto = float(request.form['peso_bulto'])
    precio_bulto = float(request.form['precio_bulto'])
    precio_arena = float(request.form['precio_arena'])
    precio_grava = float(request.form['precio_grava'])
    precio_agua = float(request.form['precio_agua'])

    cemento = 0.25
    arena = 0.35
    grava = 0.40
    agua = 180

    bultos = round((volumen * cemento * 1000) / peso_bulto, 2)
    arena_total = round(volumen * arena, 2)
    grava_total = round(volumen * grava, 2)
    agua_total = round(volumen * agua, 2)

    costo_total = round(
        (bultos * precio_bulto) + 
        (arena_total * precio_arena) + 
        (grava_total * precio_grava) + 
        (agua_total * precio_agua), 2
    )

    return render_template(
        'resultado.html',
        volumen=volumen,
        bultos=bultos,
        arena=arena_total,
        grava=grava_total,
        agua=agua_total,
        costo_total=costo_total
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



