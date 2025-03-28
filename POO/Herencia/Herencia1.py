class Persona: 
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"nombre: {self.nombre}, edad: {self.edad}"
class Carrera:
    def __init__(self,nombre,anios):
        self.nombre = nombre
        self.anios = anios
    
    def __str__(self):
        return f"nombre: {self.nombre}, anios: {self.anios}"

# no se usa Extends
class Estudiante(Persona): # un estudiante hereda de persona

    # se asume que carreras sera el objeto en forma de array(aunque cuesta acostumbrarse)
    def __init__(self, nombre, edad,nota_media, carreras):
        super().__init__(nombre, edad)
        self.nota_media = nota_media
        self.carreras = carreras
    
    def __str__(self):
        carreras_str = "\n ".join(str(carrera) for carrera in self.carreras )
        return f"{super().__str__()} Nota media: {self.nota_media},\n carreras \n {carreras_str}"

carrera1 = Carrera("Ingenieria de Software",5)
carrera2 = Carrera("Ingenieria de Sistemas",4)

estudiante = Estudiante("Fernando",23,5.4,[carrera1,carrera2])

# el instance of
print (estudiante)

objPersona = Persona("fernando",23)
objEstudiante = Estudiante("fernando",23,23.45,carrera1) 
print(isinstance(objPersona,Persona)) #sera el objeto persona una instancia de la clase Persona, saldra que si
print(isinstance(objPersona,Estudiante)) #sera el objeto persona es una instancia de Estudiante, saldra que no
print(isinstance(objEstudiante,Estudiante))# sera que el objeto estudiante es una instancia de estudiante, saldra que si
print(("si" if isinstance(objEstudiante,Persona) else "no"))#sera que el objeto estudiante es una instancia de persona, saldra que si

#para saber las subclases


print(issubclass(Estudiante, Persona))  # True
print(issubclass(Persona, Estudiante))  #  False

arreglo = []
if arreglo == []:
    print("Esta vacio")
else:
    print("tiene datos")