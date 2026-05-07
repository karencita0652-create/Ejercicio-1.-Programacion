class Servicio:

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio


class ReservaSala(Servicio):

    def mostrar_servicio(self):

        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):

    def mostrar_servicio(self):

        return f"Alquiler de equipo: {self.nombre}"


class Asesoria(Servicio):

    def mostrar_servicio(self):

        return f"Asesoría: {self.nombre}"
