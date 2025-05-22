class Pago:
    def __init__(self, id=None, hipoteca_id=None, monto=None, fecha_pago=None):


        if id is not None and (not isinstance(id, int) or id <= 0):
            raise ValueError("El id debe ser un entero positivo o None.")
        if hipoteca_id is None or hipoteca_id < 0:
            raise ValueError("El hipoteca_id debe ser un entero positivo.")
        if monto is None or monto < 0:
            raise ValueError("El monto debe ser un número positivo.")
        
        self.id = id
        self.hipoteca_id = hipoteca_id
        self.monto = monto
        self.fecha_pago = fecha_pago

    def __repr__(self):
        return (
            f"Pago(id={self.id}, hipoteca_id={self.hipoteca_id}, monto={self.monto}, fecha_pago='{self.fecha_pago}')"
        )