#------------------------------
#Problematica
        #El usuario quiere saber el area de un circulo teniendo el radio del mismo
#------------------------------
#Algoritmo:
#        //Paso 1: Solicitar al usuario que ingrese el radio del circulo
#        //Paso 2: Calcular el area usando la formula PI*Radio^2
#        //Paso 3: Mostrar el area calculada
#------------------------------
#Pseudocodigo

#Inicio
#        //Paso 1: Solicitar al usuario que ingrese el radio del circulo
#        Mostrar mensaje: "Por favor, ingrese el radio del circulo".
import math


radio = float(input("Ingrese el radio del circulo: "))
#        Leer el dato ingresado y asignarlo a variable_radio
#        //Paso 2: Calcular el area usando la formula PI*Radio^2
#        Definir y asignar a la variable area el resultado usando la formula pi*Radio^2
area = math.pi * (radio**2) 
#        //Paso 3: Mostrar el area calculada
#        Mostrar mensaje: "El area del circulo con radio", radio, "es", area
print ("El area del circulo con el radio ", radio, "es: ", area)
#Fin del programa    