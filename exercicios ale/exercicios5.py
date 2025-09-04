#5. **Soma dos números pares**
# Crie uma função que receba uma lista de números inteiros. A função deve somar apenas
# os números pares presentes na lista e retornar o resultado da soma.


def soma_numeros_pares(lista):
 soma = 0
 for numero in lista:
     if numero % 2 == 0:
         soma += numero
 return soma
print(soma_numeros_pares([1, 2, 3, 4, 5, 6]))
    