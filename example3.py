#Try combination variable exercises

'''minombre = "Monii"
mensaje = "Hola {0}!! Que tal tu dia??".format(minombre)
print ( mensaje)'''


nombre = input("¿Cual es tu nombre?: ")
print ("Hola " + nombre + " bienvenida a Python")
edad = int(input("¿Que edad tienes?: "))
num_mayor = int(edad)
if num_mayor>17:
    print ("Eres mayor de edad")
else:
    print ("Eres menor de edad")
distrito = input("¿En que distrito vives?: ")
mensaje = nombre + " vives en {0}".format(distrito) + " y tienes {0} años.".format(edad)
print (mensaje)
