# Header and Footer

def start():
    print("\n====================================================================================================== START ======================================================================================================\n")

def end():
    print("\n======================================================================================================= END =======================================================================================================")

# Detalhes dos Exercícios

# 01 - Função Dobro
'''Crie uma função que receba um número como argumento e retorne o dobro desse número. Teste a função com diferentes valores para garantir que 
está funcionando corretamente.'''

def dobro(num):
    return num*2

def ex01():
    dobro_numero = float(input("Digite um numero para receber o seu valor dobrado: "))
    print("O dobro de %f é %f." % (dobro_numero, dobro(dobro_numero)))

# 02 - Mensagem Personalizada
'''Solicite ao usuário que digite seu nome e sua idade. Após receber essas informações, exiba uma mensagem de boas-vindas personalizada, 
incluindo o nome e a idade informados.'''

def ex02():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))

    print("Bem-vindo, %s! Voce tem %d anos de idade!" % (nome, idade))

# 03 - Lista de Frutas
'''Crie uma lista contendo cinco nomes de frutas diferentes. Mostre apenas as três primeiras frutas da lista, utilizando o conceito de fatiamento 
de listas.'''

def ex03():
    lista = []

    for i in range(5):
        fruta = input("Digite a %d° fruta: " % (i+1))
        lista.append(fruta)

    print("As tres primeiras frutas sao:", lista[:3])

# 04 - Dicionário Livro
'''Crie um dicionário chamado "livro" com três informações: título, autor e ano de publicação. Mostre apenas o nome do autor utilizando o acesso 
por chave do dicionário.'''

def ex04():
    livro = {"title":"Sword of Destiny", "author":"Andrzej Sapkowski", "published":"1992"}
    print("Nome do autor de 'Sword of Destiny': ", livro.get("author"))

# 05 - Soma dos Números Pares
'''Crie uma função que receba uma lista de números inteiros. A função deve somar apenas os números pares presentes na lista e retornar o resultado 
da soma.'''

def soma_numeros_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

def ex05():
    lista = list(range(11))
    print("Soma dos números pares presentes na lista: ", soma_numeros_pares(lista))

# Main

x = int(input("\nDigite o exercicio desejado (1-5): "))

start()

if x == 1:
    ex01()
    end()
elif x == 2:
    ex02()
    end()
elif x == 3:
    ex03()
    end()
elif x == 4:
    ex04()
    end()
elif x == 5:
    ex05()
    end()
else:
    print("Erro! Exercicio Invalido.")