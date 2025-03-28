# de numero a cadena ->str(int)
num = 100
texto = str(num)  # "100"
print(texto,type(texto))  # 100 <class 'str'>

# de cadena a numero
#type para saber que tipo es
print(int(texto),type(int(texto)))


#de string a float -> str(float)
real = 12.342
texto = str(real)
print(texto,type(texto))  # 100 <class 'str'>

#de float a string -> float(texto)
print(float(texto),type(float(texto)))


print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False (cadena vacía es False)
print(bool("Hola"))  # True

#en python 0, none , "" y [] son false todo lo demas es true