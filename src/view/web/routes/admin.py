from flask import Blueprint, redirect, url_for, flash
import sys
sys.path.append("src")

from controller.ClientesController import ClientesController
from controller.PropiedadesController import PropiedadesController
from controller.HipotecasController import HipotecasController
from controller.PagosController import PagosController

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/crear_tablas')
def crear_tablas():
    try:
        ClientesController.crear_tabla()
        PropiedadesController.crear_tabla()
        HipotecasController.crear_tabla()
        PagosController.crear_tabla()
        flash("¡Tablas creadas correctamente!", "success")
    except Exception as e:
        flash(f"Error al crear tablas: {e}", "danger")
    return redirect(url_for('index.index'))

@admin_blueprint.route('/eliminar_tablas')
def eliminar_tablas():
    try:
        # El orden importa por las claves foráneas
        PagosController.eliminar_tabla()
        HipotecasController.eliminar_tabla()
        PropiedadesController.eliminar_tabla()
        ClientesController.eliminar_tabla()
        flash("¡Tablas eliminadas correctamente!", "success")
    except Exception as e:
        flash(f"Error al eliminar tablas: {e}", "danger")
    return redirect(url_for('index.index'))