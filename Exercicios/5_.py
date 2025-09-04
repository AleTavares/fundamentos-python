def inteiro (lista):
    soma = 0
    for x in lista:
        if x%2 == 0:
            soma = soma + x
    return soma

resultado = inteiro([1,2,3,4,5,6,7,8,9,10])

print(resultado)