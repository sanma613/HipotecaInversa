from flask import Blueprint, render_template, request, redirect, url_for
import sys

sys.path.append ("src")
from controller.ClientesController import ClientesController
from controller.PropiedadesController import PropiedadesController

eliminar_blueprint = Blueprint('eliminar_blueprint', __name__)

@eliminar_blueprint.route("/eliminar", methods=["POST", "GET"])
def eliminar():
    if request.method == "POST":
        tipo = request.form["tipo"]
        id = request.form["id"]

        if tipo == "cliente":
            clientesController = ClientesController()
            clientesController.eliminarbyid(id)
            mensaje = "Cliente eliminado exitosamente."
        elif tipo == "propiedad":
            propiedadesController = PropiedadesController()
            propiedadesController.eliminarbyid(id)
            mensaje = "Propiedad eliminada exitosamente."
        else:
            error = "Tipo no válido."
            return render_template("eliminar.html", error=error)

        return render_template("eliminar.html", mensaje=mensaje)

    return render_template("eliminar.html")
