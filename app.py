from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    volumen = float(request.form['volumen'])
    peso_bulto = float(request.form['peso_bulto'])
    precio_bulto = float(request.form['precio_bulto'])
    precio_arena = float(request.form['precio_arena'])
    precio_grava = float(request.form['precio_grava'])
    precio_agua = float(request.form['precio_agua'])

    # Valores por metro cúbico de mezcla
    cemento = 386.36
    agua = 170.0
    arena = 0.263
    grava = 0.428

    cemento_total_kg = cemento * volumen
    agua_total_litros = agua * volumen
    arena_total_m3 = arena * volumen
    grava_total_m3 = grava * volumen
    bultos_necesarios = cemento_total_kg / peso_bulto

    costo_cemento = bultos_necesarios * precio_bulto
    costo_arena = arena_total_m3 * precio_arena
    costo_grava = grava_total_m3 * precio_grava
    costo_agua = agua_total_litros * precio_agua
    costo_total = costo_cemento + costo_arena + costo_grava + costo_agua

    return render_template("resultado.html", volumen=volumen, bultos=round(bultos_necesarios, 2),
                           arena=round(arena_total_m3, 3), grava=round(grava_total_m3, 3),
                           agua=round(agua_total_litros, 1), costo_total=round(costo_total, 2))

if __name__ == '__main__':
    app.run(debug=True)
