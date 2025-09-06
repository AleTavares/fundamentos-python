#5. **Soma dos números pares**
#- Crie uma função que receba uma lista de números inteiros. A função deve somar apenas os números pares presentes na lista e retornar o resultado da soma.

lista_numeros = input("Digite uma lista de números inteiros separados por espaço: ") 
soma_pares = 0 #armazena um valor +-
numeros = lista_numeros.split() #separa os números que o usuário digitou em uma lista
for num in numeros: 
    if int(num) % 2 == 0: #se o número for par
        soma_pares += int(num) #soma os números pares
print("A soma dos números pares é:", soma_pares)
