def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos "+ tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #redondeamos a dos decimales utilizando la funcion round
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dolares")

#se utlizan comillas triples para indicar que todo lo que esta dentro de las comillas es un string
menu = """
Bienvenidos al conversor de monedas 💰💰💰


1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor ("colombianos", 3875)
elif opcion == 2:
   conversor ("argentinos", 65)
elif opcion == 3:
    conversor ("Mexicanos",22)
else:
    print('Opcion no valida')