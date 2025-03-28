nombre = "edad"
edad = 25
mensaje = f"Es como un template String, aqui va el nombre: {nombre} , aqui va la edad: {edad}"
print(mensaje)

#otra forma de imprimir
mensaje = "Hola, soy {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Hola, soy Ana y tengo 25 años.
