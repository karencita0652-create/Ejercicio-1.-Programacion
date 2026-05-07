from modelos.cliente import Cliente
from modelos.servicios import ReservaSala
from modelos.reserva import Reserva
from utils.logger import registrar_error


print("INICIO DEL SISTEMA")


# CLIENTE 1 CORRECTO
try:

    cliente1 = Cliente("Juan", "juan@gmail.com", 25)

    servicio1 = ReservaSala("Sala VIP", 100)

    reserva1 = Reserva(cliente1, servicio1)

    print(reserva1.mostrar_reserva())

    print(reserva1.confirmar())

except Exception as e:

    print("Error:", e)

    registrar_error(str(e))


# CLIENTE 2 CON CORREO MALO
try:

    cliente2 = Cliente("Ana", "correo_malo", 22)

except Exception as e:

    print("Error:", e)

    registrar_error(str(e))


# CLIENTE 3 MENOR DE EDAD
try:

    cliente3 = Cliente("Pedro", "pedro@gmail.com", 15)

except Exception as e:

    print("Error:", e)

    registrar_error(str(e))

finally:
    
print("EL SISTEMA SIGUE FUNCIONANDO")
