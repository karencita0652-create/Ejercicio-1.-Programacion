class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"


    def confirmar(self):

        self.estado = "Confirmada"

        return "Reserva confirmada"


    def mostrar_reserva(self):

        return f"{self.cliente.nombre} reservó {self.servicio.nombre}"
