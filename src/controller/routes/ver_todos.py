from flask import Blueprint, render_template
import sys
sys.path.append("src")

from controller.ClientesController import ClientesController
from controller.PropiedadesController import PropiedadesController
from controller.HipotecasController import HipotecasController
from controller.PagosController import PagosController

ver_todos_blueprint = Blueprint('ver_todos', __name__)

@ver_todos_blueprint.route('/clientes')
def ver_clientes():
    clientes = ClientesController.listar_todos()
    return render_template('ver_clientes.html', clientes=clientes)

@ver_todos_blueprint.route('/propiedades')
def ver_propiedades():
    propiedades = PropiedadesController.listar_todos()
    return render_template('ver_propiedades.html', propiedades=propiedades)

@ver_todos_blueprint.route('/hipotecas')
def ver_hipotecas():
    hipotecas = HipotecasController.listar_todos()
    return render_template('ver_hipotecas.html', hipotecas=hipotecas)

@ver_todos_blueprint.route('/pagos')
def ver_pagos():
    pagos = PagosController.listar_todos()
    return render_template('ver_pagos.html', pagos=pagos)