#Exercicio 01 de multiplicação, dobrando o valor das variaveis
def dobro(numero):
    resultado = numero * 2
    return resultado
total = dobro (20 * 2)
print(f"O dobro do numero {total} ")

def dobro(numero):
    resultado = numero * 2
    return resultado
total_02 = dobro (50 * 2)
print(f"O dobro do numero {total_02}")

def dobro(numero):
    resultado = numero * 2
    return resultado
total_03 = dobro (50 * 2)
print(f"O dobro do numero {total_03}")

#Exercicio 02 
def saudar(nome, idade):
    return f"ola {nome}, seu quarto corresponde a sua idade{idade}"
mensagem = saudar("nome", "idade")
print(mensagem)



print(f"Seja Bem vindo {nome}, seu quarto é de acordo com sua {idade}")

#Exercicio 03 Colocando o nomes das frutas em forma de lista
frutas = ["Abacaxi", "Maracuja", "Morango", "Uva", "Pera"]
print(f"Tres primeiras frutas: {frutas[0:3]}")

#Exercicio 04 Colocando em forma de Dicionario
livro = {"titulo": "turma da monica", "autor": "mauricio", "ano": 1959}
print(f"Nome do autor {livro["autor"]}")


def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

