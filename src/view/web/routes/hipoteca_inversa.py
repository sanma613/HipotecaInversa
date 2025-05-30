from flask import Blueprint, render_template, request
import sys

sys.path.append("src")
from model.hipoteca_inversa import Hipoteca

hipoteca_blueprint = Blueprint('hipoteca_blueprint', __name__)

@hipoteca_blueprint.route("/calcular_hipoteca", methods=["POST", "GET"])
def calcular_hipoteca():
    if request.method == "POST":
        try:
            edad = int(request.form["edad"])
            total_cuotas = int(request.form["total_cuotas"])
            precio_vivienda = float(request.form["precio_vivienda"])
            porcentaje_precio_real = float(request.form["porcentaje_precio_real"])
            tasa_interes_mensual = float(request.form["tasa_interes_mensual"])

            hipoteca = Hipoteca(edad, precio_vivienda, porcentaje_precio_real, total_cuotas, tasa_interes_mensual)

            ingreso_mensual = hipoteca.calcular_ingreso_mensual()
            deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

            return render_template("calcular_hipoteca.html", 
                                   ingreso_mensual=f"{ingreso_mensual:.0f}",
                                   deuda_total=f"{deuda_total:.0f}", )
                                   
        except Exception as e:
            error = f"Error en los datos ingresados: {str(e)}"
            return render_template("calcular_hipoteca.html", error=error)

    return render_template("calcular_hipoteca.html")