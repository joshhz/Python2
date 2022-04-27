#print ("mensaje especial")
#print ("estoy aprendiendo funciones:")
#print ("mensaje especial")
#print ("estoy aprendiendo funciones:")
#print ("mensaje especial")
#print ("estoy aprendiendo funciones:")

#def imprimir_mensajes(): #utilizamos def para definir una funcion
#    print ("mensaje especial")
#    print ("estoy aprendiendo funciones:")
    
#imprimir_mensajes()
#imprimir_mensajes()

#def conversacion(mesanje):
#    print("Hola")
#    print("cómo estas")
#    print(mesanje)
#    print("Adios")

#opcion = int(input("elige un numero: 1, 2, 3: "))  #utilizamos int para convertir la variable en un numero

#if opcion == 1:
#    conversacion("elegiste la opcion 1")
#elif opcion == 2:
#    conversacion("elegiste la opcion 2")
#elif opcion == 3:
#    conversacion("elegiste la opcion 3")
#else:
#   print("opcion no valida")

def suma (a, b): #definimos la funcion suma
    print("se suman 2 numeros")
    resultado = a + b
    return resultado #retornamos el resultado
sumatoria = suma(2, 3) #llamamos a la funcion suma
print(sumatoria) #imprimimos el resultado de la funcion suma
