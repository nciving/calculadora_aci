from flask import Flask, render_template, request

app = Flask(__name__)

# =====================
# Página principal
# =====================
@app.route("/")
def home():
    return render_template("home.html")


# =====================
# SECCIÓN ACI
# =====================
@app.route("/aci")
def aci():
    return render_template("aci.html")

@app.route("/calcular_aci", methods=["POST"])
def calcular_aci():
    try:
        volumen = float(request.form["volumen"])
        peso_bulto = float(request.form["peso_bulto"])
        precio_bulto = float(request.form["precio_bulto"])
        precio_arena = float(request.form["precio_arena"])
        precio_grava = float(request.form["precio_grava"])
        precio_agua = float(request.form["precio_agua"])

        # Resultados simulados por ahora (puedes conectar tu lógica real)
        resultado = {
            "cemento": round(volumen * 320 / peso_bulto, 2),
            "arena": round(volumen * 0.48, 2),
            "grava": round(volumen * 0.96, 2),
            "agua": round(volumen * 180, 2),  # en litros
            "costo_total": round(
                (volumen * 320 / peso_bulto) * precio_bulto +
                (volumen * 0.48) * precio_arena +
                (volumen * 0.96) * precio_grava +
                (volumen * 180) * precio_agua,
                2
            )
        }

        return render_template("resultado_aci.html", resultado=resultado)

    except Exception as e:
        return f"⚠️ Error en formulario ACI: {str(e)}"


# =====================
# SECCIÓN MUROS
# =====================
@app.route("/muros")
def muros():
    return render_template("muros.html")

@app.route("/calcular_muro", methods=["POST"])
def calcular_muro():
    try:
        H = float(request.form["H"])
        gamma_suelo = float(request.form["gamma_suelo"])
        phi = float(request.form["phi"])
        alpha = float(request.form["alpha"])
        beta = float(request.form["beta"])
        gamma_concreto = float(request.form["gamma_concreto"])

        resultado = {
            "H": H,
            "gamma_suelo": gamma_suelo,
            "phi": phi,
            "alpha": alpha,
            "beta": beta,
            "gamma_concreto": gamma_concreto
        }

        return render_template("resultado_muros.html", resultado=resultado)

    except Exception as e:
        return f"⚠️ Error en formulario Muro: {str(e)}"


# =====================
# Ejecutar app
# =====================
if __name__ == "__main__":
    app.run(debug=True)



