from excepciones.excepciones import ClienteInvalidoError


class Cliente:

    def __init__(self, nombre, email, edad):

        self.nombre = nombre
        self.email = email
        self.edad = edad

        if "@" not in email:

            raise ClienteInvalidoError("Correo inválido")

        if edad < 18:

            raise ClienteInvalidoError("El cliente debe ser mayor de edad")
