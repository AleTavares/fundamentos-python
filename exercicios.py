# Exercicio 1
def dobro(num1):
    resultado = num1 * 2
    return resultado


print(f"Exercicio 1 (dobro): ", (dobro(6))) 


#Exercicio 2
def nome_idade(nome, idade):
    return print(f"Exercício 2 (boas-vindas): Bem-vindo ", {nome}, " com idade: ", {idade})

nome_idade("Felipe", 21)


#Exercicio 3
def lista_de_frutas(x):
    lista = ['banana', 'maça', 'uva', 'cereja', 'tomate']
    return print(f"Exercicio 3 (lista de frutas): ", {lista[0]}, {lista[1]}, {lista[2]})

lista_de_frutas(1)


# Exercicio 4

livro = {
        "titulo": "O hacker",
        "autor": "Felipe",
        "ano_de_publicacao": 2020
    }
print(f"Exercicio 4: (dicionario): ", {livro["autor"]})


#Exercicio 5
def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma = soma + numero
    return soma

print(f"Exercicio 5 (soma dos pares): ", {soma_pares([1, 2, 3, 4, 5, 6])})

