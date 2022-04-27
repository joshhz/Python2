def run():
    LIMITE = 1000 #en myusculas es una constante
    
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
         print('2 elevado a ' +str(contador) + ' es igual a '+ str(potencia_2))
         contador = contador + 1
         potencia_2 = 2**contador


if __name__ == '__main__':
    run()
#contador = 0
#print('2 elevado a ' +str(contador) + ' es igual a '+ str(2**contador)
#for contador in range(0,1000):
# print('2 elevado a ' +str(contador) + ' es igual a '+ str(2**contador))