from modelos.cliente import Cliente
from modelos.servicios import ReservaSala
from utils.logger import registrar_error

try:

    cliente1 = Cliente("Juan", "juan@gmail.com", 25)

    servicio1 = ReservaSala("Sala VIP", 100)

    print(cliente1.nombre)

    print(servicio1.mostrar_servicio())

except Exception as e:

    print("Error:", e)

    registrar_error(str(e))
