from flask import Blueprint, render_template, request, redirect, url_for
import sys

sys.path.append ("src")
from controller.ClientesController import ClientesController
from controller.PropiedadesController import PropiedadesController

eliminar_blueprint = Blueprint('eliminar_blueprint', __name__)

@eliminar_blueprint.route ("/eliminar_cliente", methods=["POST", "GET"])
def eliminar_cliente():
    if request.method == "POST":
        id = request.form["id"]
        clientesController = ClientesController()
        clientesController.eliminar(id)
        return redirect(url_for("index_blueprint.index"))
    return render_template("eliminar.html")

@eliminar_blueprint.route ("/eliminar_propiedad", methods=["POST", "GET"])
def eliminar_propiedad():
    if request.method == "POST":
        id = request.form["id"]
        propiedadesController = PropiedadesController()
        propiedadesController.eliminar(id)
        return redirect(url_for("index_blueprint.index"))
    return render_template("eliminar.html")
