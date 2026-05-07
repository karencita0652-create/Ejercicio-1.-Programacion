from modelos.cliente import Cliente
from modelos.servicios import ReservaSala
from modelos.reserva import Reserva
from utils.logger import registrar_error

try:

    cliente1 = Cliente("Juan", "juan@gmail.com", 25)

    servicio1 = ReservaSala("Sala VIP", 100)

    reserva1 = Reserva(cliente1, servicio1)

    print(reserva1.mostrar_reserva())

    print(reserva1.confirmar())

except Exception as e:

    print("Error:", e)

    registrar_error(str(e))
