class Pago:
    def __init__(
        self,
        id: int,
        hipoteca_id: int,
        monto: float,
        fecha_pago: str = None
    ):
        if id is None or id < 0:
            raise ValueError("El id debe ser un entero positivo.")
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
            f"Pago(id={self.id}, hipoteca_id={self.hipoteca_id}, "
            f"monto={self.monto}, fecha_pago='{self.fecha_pago}')"
        )