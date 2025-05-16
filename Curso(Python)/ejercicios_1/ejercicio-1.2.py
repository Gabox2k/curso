#a)Pedirle al usuario que diga cualquier texto real y:
# -Calcular cuanto tardaria en decir esa frase
# - ¿Cuantas palabras digo?
# b) Si se tarda mas de 1 minuto:
# - Decirle "Tampoco te pedi un testamento"

#Le pedimos al usuario decir una frase
palabras_usuario = input("Decir una frase: ")

#Creamos un lista, usamos len() para ver la cantidad de palabras y calculamos cuanto tardaria en decir la palabra
cantidad_de_palabras= len(palabras_usuario.split())
print(f"Dijiste  {cantidad_de_palabras} palabras y tardarias {int(cantidad_de_palabras/2)} segundos en dicirlo ")


#en caso si tarda mas  de 1 minuto, le decimos "Tampoco te pide un testamento"
if cantidad_de_palabras  > 120:
   print("Tampoco te pide un testamento")
  
