# Ex 1 - Função Dobro
# Crie uma função que receba um número como argumento e retorne o dobro desse número. Teste a função com diferentes valores para garantir que está funcionando corretamente.

def double(num):
    num2 = num * 2
    return f"O dobro do número inserido é: {num2}"

num = float(input("Insira um número: "))

print(double(num))

# Ex. 2 - Mensagem personalizada

#Solicite ao usuário que digite seu nome e sua idade. Após receber essas informações, exiba uma mensagem de boas-vindas personalizada, incluindo o nome e a idade informados.

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

print(f"Olá, {nome}! Sua idade é: {idade}")

# Ex. 3 - Lista de frutas

#Crie uma lista contendo cinco nomes de frutas diferentes. Mostre apenas as três primeiras frutas da lista, utilizando o conceito de fatiamento de listas.

frutas = ["uva", "pera", "banana", "maracujá", "morango"]

print(f"As três primeiras frutas da lista são: {frutas[0:3]}")

# Ex. 4 - Dicionário livro

#Crie um dicionário chamado "livro" com três informações: título, autor e ano de publicação. Mostre apenas o nome do autor utilizando o acesso por chave do dicionário.

livro = {
    "titulo":"Jantar Secreto",
    "autor":"Raphael Montes",
    "ano de publicacao":"2016"
}

print(f"O nome do autor é: {livro['autor']}")

# Ex. 5 - Soma dos números pares

#Crie uma função que receba uma lista de números inteiros. A função deve somar apenas os números pares presentes na lista e retornar o resultado da soma.

numeros = [1, 2, 3, 4, 5]

def soma_pares(numeros):
    soma = 0
    for num in numeros:
        if num%2==0:
            soma += num
    return soma

print(f"A soma dos números pares é: {soma_pares(numeros)}")