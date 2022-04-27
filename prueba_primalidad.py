# def es_primo(numero):
#     if numero == 1:
#         return False
#     else:
#         contador = 0
#     for i in range(1,numero+1):
       
#         if numero % i == 0:
#             contador += 1 
#         elif contador == 2 and i < numero:
#             print('no es primo:')
#             break
#     if contador == 1:
#         print('no es primo')
#     elif contador == 2 and i == numero:
#         print('es primo')

# def run():
#     numero = int(input('Ingresa un numero: '))
    
#     es_primo(numero)
      

# if __name__ == '__main__':
#     run()
def es_primo(numero):
    if numero == 1:
        return False
    else:
        contador = 0
    for i in range(1 , numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print(str(numero) + " es primo")
    else:
        print(str(numero) +  " NO es primo")


if __name__ == "__main__":
    run()