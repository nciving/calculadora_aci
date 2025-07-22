
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para ACI
@app.route('/aci')
def aci():
    return render_template('aci.html')

# Ruta para Muros
@app.route('/muros')
def muros():
    return render_template('muros.html')

# Ruta para procesar cálculo de muros
@app.route('/calcular_muro', methods=['POST'])
def calcular_muro():
    try:
        H = float(request.form["H"])
        gamma_suelo = float(request.form["gamma_suelo"])
        phi = float(request.form["phi"])
        beta = float(request.form["beta"])
        gamma_concreto = float(request.form["gamma_concreto"])

        import math
        Ka = (math.cos(math.radians(phi)) - math.sqrt((math.cos(math.radians(phi)))**2 - (math.cos(math.radians(beta)))**2)) / (math.cos(math.radians(beta)) + math.sqrt((math.cos(math.radians(phi)))**2 - (math.cos(math.radians(beta)))**2))
        Ea = 0.5 * Ka * gamma_suelo * H**2

        resultado = {
            "H": H,
            "gamma_suelo": gamma_suelo,
            "phi": phi,
            "beta": beta,
            "Ka": round(Ka, 3),
            "Ea": round(Ea, 2),
        }

        return render_template("resultado_muros.html", resultado=resultado)

    except Exception as e:
        return f"⚠️ Error en el cálculo: {str(e)}"

# Activar app en Render correctamente
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



