#Ingresa tu nombre e imprime saludo
nombre = input("What is your name?: ")
print ("Hello {0}".format(nombre))

#Calcular la hipotenusa de un triangulo rectangulo
a = int(input("Escriba el cateto mayor: "))
b = int(input("Escriba el cateto menor: "))
c = ((a*a)+(b*b))**(1/2)
print("La hipotenusa es: {0}".format(c))

#Calcular el volumen de una esfera
a = int(input("Ingresa el radio(m) de la esfera: "))
v = ((4/3)*3.1416*((a)**3))
print("El volumen de la esfera es: {0}".format(v))

#Calcular el IGV (18%) de un monto
a = int(input("Ingrese el monto: "))
igv = (0.18*a)
print("El IGV de " + str(a) +  " es: {0}".format(igv))

#Dado un monto en soles, conviertelo a dolares y a euros
a = int(input("Ingrese el monto(en soles): "))
d = (a*0.30)
e = (a*0.27)
print("Su monto en dolares es : {0}".format(d))
print("Su monto en euros es: {0}".format(e))