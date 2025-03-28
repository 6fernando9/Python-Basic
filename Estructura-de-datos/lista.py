# lista variada
#tda lista
mi_lista = [1, 2, 3, "Hola", True]

#metodos de la lista
print(mi_lista[0])  # 1
mi_lista.append(4)   # Agrega al final
mi_lista.remove(2)   # Elimina el valor 2
print(mi_lista)      # [1, 3, 'Hola', True, 4]



mi_lista.pop()     # Elimina el último elemento
mi_lista.insert(1, "Nuevo")  # Inserta en el índice 1
mi_lista.reverse() # Invierte la lista
mi_lista.sort()    # Ordena la lista (solo si son del mismo tipo)
