def registrar_error(mensaje):

    archivo = open("logs.txt", "a")

    archivo.write(mensaje + "\n")

    archivo.close()
