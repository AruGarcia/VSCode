def contar_caracteres(s):
    """Função para contar os caracteres de uma string
    ex:

    #>>> contar_caracteres('aruana')
    a: 3
    n: 1
    r: 1
    u: 1
    :param s:  string a ser contada
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')

contar_caracteres("gegsadf")
print()
contar_caracteres("Abacate")
print()