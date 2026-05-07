from modelos.cliente import Cliente
from utils.logger import registrar_error

try:

    cliente1 = Cliente("Ana", "correo_malo", 20)

except Exception as e:

    print("Ocurrió un error:", e)

    registrar_error(str(e))

print("El programa sigue funcionando")
