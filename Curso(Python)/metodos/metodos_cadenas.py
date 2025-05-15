cadena1= "Hola,como,estas"
cadena2= "bien"

#convierte a mayusucla
mays= cadena1.upper()

#convierte a minuscula
minis= cadena1.lower()

#primera letra en mayuscula
primer= cadena2.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidenci devuelve -1
busqueda_find= cadena1.find("e")

#buscamos una cadena en otra cadena, si no hay coincedencias lanza un error
busqueda_index= cadena1.index("H")

#si es numerico devuelve true, sino devuelve False
numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true, sino devuelve false
numerc_alfa= cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias 
contar_coincidencia= cadena1.count("H")

#contamos cuanto caracteres tiene una cadena
contar_carac= len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True 
empezar= cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True 
termina= cadena1.endswith("la")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva= cadena1.replace("," , " ")

#separar cadenas con la cadena que le pasemos
cadena_separada= cadena1.split(",")

print(cadena_separada)