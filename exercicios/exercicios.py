

#soma dos pares

def somapares(numeros):
    resultado = 0
    for x in numeros:
        if x % 2 == 0:
            resultado += x
    return resultado

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"A soma dos pares é: {somapares(lista)}")

