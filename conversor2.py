 #creamos una variable donde pedimos al usuario que ingrse la cantidad de dolares que desea convertir
dolares = input("Ingrese la cantidad de dolares: ")
#convertimos la variable dolares a float
dolares = float(dolares)
#asignamos el valor de variavle pesos 
valor_pesos = .049
#realizamos la operacion para convertir dolares a pesos
pesos = dolares / valor_pesos
pesos = round(pesos,2) #redondeamos el resultado a dos decimales
pesos = str(pesos)

print("Tienes $ "+ pesos + ' pesos')

