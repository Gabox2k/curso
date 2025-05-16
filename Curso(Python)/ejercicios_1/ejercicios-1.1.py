# a)Diferencia en porcentaje entre el curso actual y:
# -el mas rapido de otros cursos
# - el mas lento de otros cursos
# - el promedio de los curso
# b) Porcentaje de material inservinle que se reduce en:
# - el promedio de los curso
# - el cruso actaul (este curso)
# c) Ver 10 hs de este curso a cuantas de otros cursos equivale


#Promedio de duracion de los cursos
otros_cursos_min = 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
video_youtube= 1.5

#Duracion de crudos (sin editar)
crudo_promedio = 5
crudo_youtube = 3.5

#diferencia de duracion
diferencia_con_min = 100 - video_youtube / otros_cursos_min *100
diferencia_con_max = 100 - video_youtube *1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - video_youtube / otros_cursos_promedio *100

#Calculando el porcentaaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio *1000 // crudo_promedio / 10
tiempo_vacio_youtube = 100 - video_youtube *1000 // crudo_youtube / 10


#Mostrando las diferencias de duracion (Ejecicio A)
print("-------------")
print(f"El curso de youtube dura {diferencia_con_min} % menos que el mas rapido")
print(f"El curso de youtube dura {diferencia_con_max} % menos que el mas lento")
print(f"El curso de youtube dura {diferencia_con_promedio} % menos que el promedio")
print("-------------")

#Mostrando la cantidad de espacios vacios que se remueven (Ejercicio B)
print("-------------")
print(f"Un curso promedio elimina un {tiempo_vacio_promedio} % de tiempo vacio")
print(f"Este curso elimino {tiempo_vacio_youtube} % de timpo vacio")
print("-------------")

#Mostrando diferencias si los cursos duraran 10 hs
print("-------------")
print(f"Ver 10 hs de este curso equivale a ver {int (otros_cursos_promedio / video_youtube *10)} hs de otros cursos")
print(f"Ver 10 hs de otros cursos equivale a ver {int (video_youtube / otros_cursos_promedio *10)} hs de este curso")
print("-------------")

