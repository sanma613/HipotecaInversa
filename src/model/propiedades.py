class Propiedad:
    def __init__(
        self,
        id: int,
        direccion: str,
        valor: float,
        tipo: str = None,
        propietario_id: int = None,
        fecha_registro: str = None
    ):
        if id is None or id < 0:
            raise ValueError("El id debe ser un entero positivo.")
        if not direccion or not isinstance(direccion, str):
            raise ValueError("La dirección es obligatoria y debe ser una cadena de texto.")
        if valor is None or valor < 0:
            raise ValueError("El valor debe ser un número positivo.")
        if tipo is not None and not isinstance(tipo, str):
            raise ValueError("El tipo debe ser una cadena de texto.")
        if propietario_id is not None and propietario_id < 0:
            raise ValueError("El propietario_id debe ser un entero positivo.")

        self.id = id
        self.direccion = direccion
        self.valor = valor
        self.tipo = tipo
        self.propietario_id = propietario_id
        self.fecha_registro = fecha_registro

    def __repr__(self):
        return (
            f"Propiedad(id={self.id}, direccion='{self.direccion}', valor={self.valor}, "
            f"tipo='{self.tipo}', propietario_id={self.propietario_id}, fecha_registro='{self.fecha_registro}')"
        )