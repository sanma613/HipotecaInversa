class Hipoteca:
    def __init__(self, id, cliente_id, propiedad_id, total_cuotas, tasa_interes_mensual, ingreso_mensual, deuda_total, fecha_inicio, estado):
        if id is not None and (not isinstance(id, int) or id <= 0):
            raise ValueError("El id debe ser un entero positivo.")
        if cliente_id is None or cliente_id <= 0:
            raise ValueError("El cliente_id debe ser un entero positivo.")
        if propiedad_id is None or propiedad_id <= 0:
            raise ValueError("El propiedad_id debe ser un entero positivo.")
        if total_cuotas is None or total_cuotas <= 0:
            raise ValueError("El total_cuotas debe ser un entero positivo mayor a cero.")
        if tasa_interes_mensual is None or tasa_interes_mensual < 0:
            raise ValueError("La tasa_interes_mensual debe ser un número positivo.")
        if ingreso_mensual is not None and ingreso_mensual < 0:
            raise ValueError("El ingreso_mensual no puede ser negativo.")
        if deuda_total is not None and deuda_total < 0:
            raise ValueError("La deuda_total no puede ser negativa.")

        self.id = id
        self.cliente_id = cliente_id
        self.propiedad_id = propiedad_id
        self.total_cuotas = total_cuotas
        self.tasa_interes_mensual = tasa_interes_mensual
        self.ingreso_mensual = ingreso_mensual
        self.deuda_total = deuda_total
        self.fecha_inicio = fecha_inicio
        self.estado = estado 

    def __repr__(self):
        return (
            f"Hipoteca(id={self.id}, cliente_id={self.cliente_id}, "
            f"propiedad_id={self.propiedad_id}, total_cuotas={self.total_cuotas}, "
            f"tasa_interes_mensual={self.tasa_interes_mensual}, ingreso_mensual={self.ingreso_mensual}, "
            f"deuda_total={self.deuda_total}, fecha_inicio={self.fecha_inicio})"
        )
