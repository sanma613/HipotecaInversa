from flask import Blueprint, render_template, request, redirect, url_for
import sys

sys.path.append ("src")
from controller.ClientesController import ClientesController
eliminar_blueprint = Blueprint('eliminar_blueprint', __name__)

@eliminar_blueprint.route ("/eliminar", methods=["POST", "GET"])
def eliminar():
    if request.method == "POST":
        id = request.form["id"]
        clientesController = ClientesController()
        clientesController.eliminar(id)
        return redirect(url_for("index_blueprint.index"))
    return render_template("eliminar.html")