def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 5898:
    #         break

    texto = input('ingresa un texto:')
    for letra in texto:
        if letra == 'a':
            break
        print(letra)
        


if __name__ == '__main__':
    run()