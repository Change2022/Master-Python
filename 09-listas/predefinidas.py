# File: predefinidas.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

pasteles = ["Chocolate", "Vainilla"," 3 leches", "Nuez", "Café"]
numeros = [1, 4, 6, 2, 5, 3, 7]

# Ordenar lista.

print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos a la lista.
print("")
pasteles.append("Chocoflan")    # Al final de la lista
pasteles.insert(2, "Frutas")    # Se especifíca el índice donde se va a guardar el nuevo elemento.
print(pasteles)

# Eliminar elementos.

pasteles.pop(1)    # Elimina un índice especifíco.
pasteles.remove("Chocoflan")    # Elimina un elemento por su nombre o valor.
print(pasteles)

# Mostrar al inverso una lista.
print("")
print(numeros)
numeros.reverse()
print(numeros)

# Buscar elementos en una lista.
print("")
print("Chocolate" in pasteles)    # Verificar sí un elemento existe en una lista.
print(10 in numeros)

print("")
print(len(pasteles))    # Contar cuantos elementos hay en una lista.
print(len(numeros))

print("")
numeros.append(2)
print(numeros.count(2))    # Contar cauntas veces aparece un elemento en una lista.

print("")
print(pasteles.index("Frutas"))    # Buscar el índice en donde se encuentra el valor de un elemento.

# Unir listas.
print("")
pasteles.extend(numeros)   # Función predefinida para extender y/o unir listas.
print(pasteles)

