from modelos.cliente import Cliente
from modelos.servicios import Servicio
from modelos.reserva import Reserva

cliente1 = Cliente("Juan", "juan@gmail.com", 25)

servicio1 = Servicio("Sala VIP", 100)

reserva1 = Reserva(cliente1, servicio1)

print(cliente1.nombre)
print(servicio1.nombre)
