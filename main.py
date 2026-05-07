from modelos.cliente import Cliente

try:

    cliente1 = Cliente("Ana", "correo_malo", 20)

except Exception as e:

    print("Ocurrió un error:", e)

print("El programa sigue funcionando")
