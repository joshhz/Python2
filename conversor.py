#creamos una variable donde el usuario ingrese el valor a convertir
pesos = input("¿cuantos pesos mexicanos tienes?: ")
#transformamos la variable en un numero decimal
pesos = float(pesos)
valor_dolar = 20.61

dolares = pesos / valor_dolar
dolares = round(dolares, 2) #redondeamos a dos decimales utilizando la funcion round
dolares = str(dolares)
print ("Tienes $" + dolares + " dolares")

