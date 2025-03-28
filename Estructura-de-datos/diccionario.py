#equivalente al JSON

mi_dict = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}
print(mi_dict["nombre"])  # Juan

mi_dict["edad"] = 26  # Modificar un valor
mi_dict["pais"] = "España"  # Agregar nueva clave
print(mi_dict.keys())   # dict_keys(['nombre', 'edad', 'ciudad', 'pais'])
print(mi_dict.values()) # dict_values(['Juan', 26, 'Madrid', 'España'])
