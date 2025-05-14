#se puede modicar
lista = ["Gabriel" , 15 , True, 1.70]
#No se puede modificar
tupla = ("Gabriel" , 15 , True, 1.70, "Gabriel")

#valido
lista[3]= 22

#no valido
#tupla[3] =22

#Conjunto  set (no se pude llamar por el indice, no almacena datos duplicados)
conjunto = {'Gabriel' , 15 , True, 1.70, "Gabriel"}
print(conjunto)

#diccionario 
diccionario = { 'nombre' : "Gabriel" ,
            'edad' : 20 ,
            'Profesion' :  "programacion",
            'altura' : 1.87
}
print(diccionario["altura"])