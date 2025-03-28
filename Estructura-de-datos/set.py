mi_set = {1, 2, 3, 3, 3} #conjunto dividido en roles y permisos
print(mi_set)  # {1, 2, 3}  (sin duplicados)

mi_set.add(4)     # Agrega un elemento
mi_set.remove(2)  # Elimina un elemento
print(mi_set)     # {1, 3, 4}


#duplicar elemento, este si parece un backend con ts

lista = [1, 2, 2, 3, 3, 4]
sin_duplicados = list(set(lista))
print(sin_duplicados)  # [1, 2, 3, 4]

