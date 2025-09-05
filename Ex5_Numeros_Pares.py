#Soma de numeros pares com uma funçao

def soma_pares(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("A soma dos números pares é:", soma_pares(lista_numeros))
    
 


