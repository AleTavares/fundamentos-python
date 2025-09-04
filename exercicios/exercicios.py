
#Função que devolve smepre o dobro
def dobro(num1):
    num1 = input("Digite o numero que voce deseja receber o resultado de dobro: ")
    num1 = int(num1)

    resultado = num1 + num1
    return resultado

total = dobro(5)
print(f"O dobro do numero é: {total}")

#------------------------------------------------------------------#
#Solicita o nome e a idade do usuário

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Seja bem-vindo(a), {nome}! Você tem {idade} anos.")

#-------------------------------------------------------------------#

#Lista de frutas

frutas = ["maçã", "banana", "cereja", "Melancia", "Pera"]
print(f"Lista atualizada: {frutas[0:3]}")

#soma dos pares

def somapares(numeros):
    resultado = 0
    for x in numeros:
        if x % 2 == 0:
            resultado += x
    return resultado

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"A soma dos pares é: {somapares(lista)}")
