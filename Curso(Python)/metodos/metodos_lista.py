#Creando una lista con lis()
lista= list([ 78 , 45 , 54, 7,False])

#devuelve la cantidad de elementos de la lista
cantidad_elementos= len(lista)

#agregando un elemento a la lista
lista.append(True)

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "Juan")

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(-2) #el -1 para eliminar el ultimo, el -2 para el anteultimo, y asi sucesivamente

#removiendo un elemento por su valor
lista.remove("Juan")

#ordenando la lista de forma ascendente(si usamos el para el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirteiendo los elementos de una lista
lista.reverse() 


#eliminando todos los elementos de la lista
lista.clear()



print(lista)