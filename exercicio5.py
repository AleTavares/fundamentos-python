def soma_pares(lista):
    return sum(x for x in lista if x % 2 == 0)

print(soma_pares([1, 2, 3, 4, 5, 6]))  # Saída: 12
