#Soma de numeros pares com uma funçao

def soma_pares(numeros):
    soma = 0
    #É o loop para percorrer a lista toda
    for num in numeros:
        #Verifica se o numero é par
        if num % 2 == 0:
            #Vai somando os pares
            soma += num 
            #Retorna a soma para fazer dnv o loop
    return soma


#Lista de numeros
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Mostra o total 
# (A lista pode ser alterada  é colocada na frente da funçao pq é ali q a funçao vai saber q é para verificar)
print("A soma dos números pares é:", soma_pares(lista_numeros))
    
 


