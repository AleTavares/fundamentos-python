# Exercício 1: Crie uma função que receba um número como argumento e retorne o dobro desse número. Teste a função com diferentes valores para garantir que está funcionando corretamente.
def mult(num):
    resultado = num * 2
    return resultado
num = input("Escreva um número: ")
print(f"O dobro do número {num} é {mult(int(num))}")

# Exercício 2: Solicite ao usuário que digite seu nome e sua idade. Após receber essas informações, exiba uma mensagem de boas-vindas personalizada, incluindo o nome e a idade informados.
name = input("Escreva seu nome: ")
id = input("Escreva sua idade: ")
print(f"Olá {name}, você tem {id} anos.")

# Exercício 3: Crie uma lista contendo cinco nomes de frutas diferentes. Mostre apenas as três primeiras frutas da lista, utilizando o conceito de fatiamento de listas.
frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print(f"As três primeiras frutas da lista são: {frutas[0:3]}")

# Exercício 4: Crie um dicionário chamado "livro" com três informações: título, autor e ano de publicação. Mostre apenas o nome do autor utilizando o acesso por chave do dicionário.
livro ={"título": "O Leão", "autor": "Paulo Pinto", "ano": 2011}
print(livro["autor"])

# Exercício 5: Crie uma função que receba uma lista de números inteiros. A função deve somar apenas os números pares presentes na lista e retornar o resultado da soma.
def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma