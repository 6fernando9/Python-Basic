texto = "Python como verduras"
print(texto.upper())  # PYTHON
print(texto.lower())  # python
print(texto.capitalize())  # Python (primera letra en mayúscula)
print(texto.title())  # Python (cada palabra con mayúscula)

texto = "  hola mundo  "
print(texto.strip())  # "hola mundo"
print(texto.lstrip())  # "hola mundo  " (izquierda)
print(texto.rstrip())  # "  hola mundo" (derecha)

texto = "Hola mundo"
print(texto.replace("mundo", "Python"))  # Hola Python

texto = "rojo,verde,azul"
colores = texto.split(",")
print(colores)  # ['rojo', 'verde', 'azul']

archivo = "documento.pdf"
print(archivo.endswith(".pdf"))  # True
print(archivo.startswith("doc"))  # True

frase = "Aprender Python es divertido"
print("Python" in frase)  # True
print("Java" in frase)  # False
