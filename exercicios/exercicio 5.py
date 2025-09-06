#Exercicio 5

    #Soma dos números pares

    ##Crie uma função que receba uma lista de números inteiros.
    ###A função deve somar apenas os números pares presentes na lista e retornar o resultado da soma.


numeros_lista = input("Digite uma lista de números inteiros separados por espaço: ");

soma_pares = 0;
numeros = numeros_lista.split();
for num in numeros:
    numero = int(num);
    if numero % 2 == 0:
        soma_pares += numero;


print("A soma dos números pares na lista é:", soma_pares);