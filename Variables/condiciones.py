#condicionales no funciona con && o || , funciona con el and y el or 
x = 12
if x >= 8 and x <= 20:
    print("El numero esta entre 8 y 20")

x = "casr"

#formato if else if else, aqui es if elif else
if x == "fernando": 
    print("eres fernando")
elif x == "Fernando":
    print("eres Fernando")
else: 
    print("no se que carajo eres")

#formato compacto de respuesta
edad = 20
mensaje =  "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

#versus
#let mensaje = edad >= 18 ? "Mayor de edad" : "Menor de edad";
#console.log(mensaje);

