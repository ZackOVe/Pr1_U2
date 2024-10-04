print("")
print("Zamarripa Castro Erick Fabián")
print("") #Espacio vacio
#Punto 1
Precios = [43, 57, 92, 20, 37, 5, 9] #Lista de digitos 
print (Precios) #Imprimira los precios
print ("El mayor precio es: ", [2]) #Mostrara el numero mayor
print ("El menor precio es: ", [5]) #Mostrara ek numero menor

#Punto 2
materias = ["Pensamiento matematico", "Español", "Ingles", "Quimica", "Humanidades", "Ecosistemas"]
print (materias)
#Espacio vacio

#Punto 3
print ("Estoy cursando: ", materias[0]) #0 sera 1 como primer materia
print ("Estoy cursando: ", materias[1]) #1 sera 2 como segunda materia
print ("Estoy cursando: ", materias[2]) #2 sera 3 como tercer materia
print ("Estoy cursando: ", materias[3]) #3 sera 4 como cuarta materia
print ("Estoy cursando: ", materias[4]) #4 sera 5 como quinta materia
print ("Estoy cursando: ", materias[5]) #5 sera 6 como sexta materia

#Punto 4
calificacion = [10, 5, 8, 5, 7 ,5] #Seran la calificacion de las 6 materias

print (calificacion) #Imprimira las calificaciones

#Se imprimiran las materias seguido de las calificaciones correspondientes
print ("En", materias[0], "has obtenido", calificacion[0]) 
print ("En", materias[1], "has obtenido", calificacion[1])
print ("En", materias[2], "has obtenido", calificacion[2])
print ("En", materias[3], "has obtenido", calificacion[3])
print ("En", materias[4], "has obtenido", calificacion[4])
print ("En", materias[5], "has obtenido", calificacion[5])
print("")

#Punto 5 
num1 = (input("Ingrese el primer numero ganador: "))
num2 = (input("Ingrese el segundo numero ganador: "))
num3 = (input("Ingrese el tercer numero ganador: "))

num = [num1, num2, num3]
num.sort()

print(num)