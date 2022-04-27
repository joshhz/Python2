import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero entre 1 y 100:'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('El numero es mayor')
        else:
            print('busca un numero mas pequeno')
        numero_elegido = int(input('Elige otro numero'))
    print('Felicidades, has adivinado el numero')            
if __name__ == '__main__':
    run()