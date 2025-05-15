diccionario = {
        "nombre" : "Juan",
        "edad" : 78,
        "Trabajo" : "programcion"
}

#nos develve un objeto dic_item
claves= diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_que= diccionario.get("que")
print("el programa funciona 10/10")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("Trabajo")

#obtiniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)