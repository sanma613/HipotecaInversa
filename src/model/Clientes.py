class Cliente:
    def __init__(
        self,
        id: int,
        nombre: str,
        edad: int,
        direccion: str = None,
        telefono: str = None,
        email: str = None,
        fecha_registro: str = None
    ):
        if id is None or id < 0:
            raise ValueError("El id debe ser un entero positivo.")
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre es obligatorio y debe ser una cadena de texto.")
        if edad is None or edad <= 0:
            raise ValueError("La edad debe ser un entero positivo mayor a cero.")
        if telefono is not None and not isinstance(telefono, str):
            raise ValueError("El teléfono debe ser una cadena de texto.")
        if email is not None and not isinstance(email, str):
            raise ValueError("El email debe ser una cadena de texto.")

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_registro = fecha_registro

    def __repr__(self):
        return (
            f"Cliente(id={self.id}, nombre='{self.nombre}', edad={self.edad}, "
            f"direccion='{self.direccion}', telefono='{self.telefono}', "
            f"email='{self.email}', fecha_registro='{self.fecha_registro}')"
        )