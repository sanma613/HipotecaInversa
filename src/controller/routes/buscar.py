from flask import Blueprint, render_template, request, redirect, url_for
import sys

sys.path.append("src")

from controller.ClientesController import ClientesController
from controller.PropiedadesController import PropiedadesController
from controller.HipotecasController import HipotecasController
from controller.PagosController import PagosController

buscar_blueprint = Blueprint('buscar', __name__)

@buscar_blueprint.route('/buscar', methods=['GET', 'POST'])
def buscar():
    error = None

    if request.method == 'POST':
        tipo = request.form.get('tipo')
        id_str = request.form.get('id')
        if not tipo or not id_str:
            error = "Debe seleccionar un tipo y un ID."
        else:
            try:
                id = int(id_str)
                return redirect(url_for('buscar.resultado_busqueda', tipo=tipo, id=id))
            except Exception as e:
                error = f"Error en la búsqueda: {str(e)}"
    return render_template('buscar.html', error=error)
    

@buscar_blueprint.route('/resultado_busqueda')
def resultado_busqueda():
    tipo = request.args.get('tipo')
    id_str = request.args.get('id')
    resultado = None
    error = None
    try:
        id = int(id_str)
        if tipo == "cliente":
            resultado = ClientesController.buscar_cliente(id)
        elif tipo == "propiedad":
            resultado = PropiedadesController.buscar_propiedad(id)
        elif tipo == "hipoteca":
            resultado = HipotecasController.buscar_hipoteca(id)
        elif tipo == "pago":
            resultado = PagosController.buscar_pago(id)
        else:
            error = "Tipo de búsqueda no válido."
        if resultado is None and not error:
            error = "No se encontró ningún registro con ese ID."
    except Exception as e:
        error = f"Error en la búsqueda: {str(e)}"
    return render_template('resultado_busqueda.html', resultado=resultado, error=error)