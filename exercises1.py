#imprime la longitud de una lista
Lista = ["chiwi","scoty","bailey","maiky","scott"]
print(len(Lista))

#Crear un diccionario sobre uno mismo (Distrito, edad, mascota)
#Llave [] ; diccionario {}
diccionario = {"nombre" : "Monica Silva", "edad" : "23 años", "distrito" : "SMP", "mascota": "chiwi"}
#forma1 de agregar
diccionario.update({"color favorito" : "azul"})
print(diccionario)
#forma2 de agregar
diccionario["enamorado"] = "harold"
print(diccionario)
#Imprimir las claves del diccionario
print(diccionario.keys())