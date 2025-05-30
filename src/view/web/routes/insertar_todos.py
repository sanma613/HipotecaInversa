from flask import Blueprint, render_template, request, flash, redirect, url_for
import sys
sys.path.append("src")
from datetime import datetime

from controller.ClientesController import ClientesController
from controller.PropiedadesController import PropiedadesController
from controller.HipotecasController import HipotecasController
from controller.PagosController import PagosController

from src.model.Clientes import Cliente
from src.model.propiedades import Propiedad
from src.model.Hipotecas import Hipoteca
from src.model.Pagos import Pago

insertar_todos_blueprint = Blueprint('insertar_todos', __name__)

# Error handler para ValueError y otros
@insertar_todos_blueprint.app_errorhandler(Exception)
def handle_insert_error(error):
    flash(f"Error: {str(error)}", "danger")
    # Redirige a la página anterior o al index si no hay referrer
    return redirect(request.referrer or url_for('index'))

@insertar_todos_blueprint.route('/insertar_cliente', methods=['GET', 'POST'])
def insertar_cliente():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        if not nombre or not edad:
            raise ValueError("Nombre y edad son obligatorios.")
        cliente = Cliente(
            id=None,
            nombre=nombre,
            edad=int(edad),
            direccion=direccion,
            telefono=telefono,
            email=email
        )
        ClientesController.insertar(cliente)
        mensaje = "Cliente insertado correctamente."
        flash(mensaje, "success")
        return redirect(url_for('insertar_todos.insertar_cliente'))
    return render_template('insertar_cliente.html')

@insertar_todos_blueprint.route('/insertar_propiedad', methods=['GET', 'POST'])
def insertar_propiedad():
    mensaje = None
    if request.method == 'POST':
        direccion = request.form.get('direccion')
        valor = request.form.get('valor')
        tipo = request.form.get('tipo')
        propietario_id = request.form.get('propietario_id')
        if not direccion or not valor or not tipo or not propietario_id:
            raise ValueError("Todos los campos son obligatorios.")
        propiedad = Propiedad(
            id=None,
            direccion=direccion,
            valor=float(valor),
            tipo=tipo,
            propietario_id=int(propietario_id)
        )
        PropiedadesController.insertar(propiedad)
        mensaje = "Propiedad insertada correctamente."
        flash(mensaje, "success")
        return redirect(url_for('insertar_todos.insertar_propiedad'))
    return render_template('insertar_propiedad.html')

@insertar_todos_blueprint.route('/insertar_hipoteca', methods=['GET', 'POST'])
def insertar_hipoteca():
    mensaje = None
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')
        propiedad_id = request.form.get('propiedad_id')
        total_cuotas = request.form.get('total_cuotas')
        tasa_interes_mensual = request.form.get('tasa_interes_mensual')
        ingreso_mensual = request.form.get('ingreso_mensual')
        deuda_total = request.form.get('deuda_total')
        fecha_inicio = request.form.get('fecha_inicio')
        estado = request.form.get('estado')
        if not all([cliente_id, propiedad_id, total_cuotas, tasa_interes_mensual, ingreso_mensual, deuda_total, fecha_inicio, estado]):
            raise ValueError("Todos los campos son obligatorios.")
        
        # Convertir fecha_inicio a datetime
        try:
            fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        except Exception:
            raise ValueError("La fecha de inicio no tiene un formato válido (YYYY-MM-DD).")
        
        hipoteca = Hipoteca(
            id=None,
            cliente_id=int(cliente_id),
            propiedad_id=int(propiedad_id),
            total_cuotas=int(total_cuotas),
            tasa_interes_mensual=float(tasa_interes_mensual),
            ingreso_mensual=float(ingreso_mensual),
            deuda_total=float(deuda_total),
            fecha_inicio=fecha_inicio_dt,
            estado=estado
        )
        HipotecasController.insertar(hipoteca)
        mensaje = "Hipoteca insertada correctamente."
        flash(mensaje, "success")
        return redirect(url_for('insertar_todos.insertar_hipoteca'))
    return render_template('insertar_hipoteca.html')

@insertar_todos_blueprint.route('/insertar_pago', methods=['GET', 'POST'])
def insertar_pago():
    mensaje = None
    if request.method == 'POST':
        hipoteca_id = request.form.get('hipoteca_id')
        monto = request.form.get('monto')
        fecha_pago = request.form.get('fecha_pago')
        if not hipoteca_id or not monto or not fecha_pago:
            raise ValueError("Todos los campos son obligatorios.")
        try:
            fecha_pago_dt = datetime.strptime(fecha_pago, "%Y-%m-%d")
        except Exception:
            raise ValueError("La fecha de pago no tiene un formato válido (YYYY-MM-DD).")
        pago = Pago(
            id=None,
            hipoteca_id=int(hipoteca_id),
            monto=float(monto),
            fecha_pago=fecha_pago_dt
        )
        PagosController.insertar(pago)
        mensaje = "Pago insertado correctamente."
        flash(mensaje, "success")
        return redirect(url_for('insertar_todos.insertar_pago'))
    return render_template('insertar_pago.html')