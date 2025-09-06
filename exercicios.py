#Crie uma função que receba um número como argumento e retorne o dobro desse número. Teste a função com diferentes valores para garantir que está funcionando corretamente.  

numero = int (input ("digite um numero: "))

def dobro(numero):
    return numero * 2 

print(dobro(numero))

#Solicite ao usuário que digite seu nome e sua idade. Após receber essas informações, exiba uma mensagem de boas-vindas personalizada, incluindo o nome e a idade informados.
nome = input("Digite seu nome:")
idade = input("Digite sua idade: ")
print(f"Seja bem-vindo {nome}, você tem {idade} anos!")

#Crie uma lista contendo cinco nomes de frutas diferentes. Mostre apenas as três primeiras frutas da lista, utilizando o conceito de fatiamento de listas.

print("Apeas as tres primeiras frutas da lista: ")
frutas =["banana", "mamao", "uva", "laranja", "abacaxi"]
print(frutas[0:3])

#Crie um dicionário chamado "livro" com três informações: título, autor e ano de publicação. Mostre apenas o nome do autor utilizando o acesso por chave do dicionário.
livro = {
    "titulo": "O Maior santista do mundo",
    "autor": "Thiago Marques",
    "ano_publicacao": 2007
}
print( "O autor do livro é: ",{livro["autor"]})

#Crie uma função que receba uma lista de números inteiros. A função deve somar apenas os números pares presentes na lista e retornar o resultado da soma.
def soma_pares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma = soma + numero
    return soma
lista_numeros = [1, 2, 3, 4, 5, 6]
resultado = soma_pares(lista_numeros)
print("A soma dos números pares é:", resultado)