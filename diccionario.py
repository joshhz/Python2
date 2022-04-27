def run():
    diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(diccionario['llave1'])
    # print(diccionario['llave2'])
    # print(diccionario['llave3'])
    
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
        'Mexico': 128932753,
    }
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais2 in poblacion_paises.values():
    #     print(pais2)
    
    for pais3, poblacion in poblacion_paises.items():
        print(pais3 + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
    run()