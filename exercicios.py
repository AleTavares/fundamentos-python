# Exercício 1: Função que retorna o dobro de um número 

def dobro(num):
    return num * 2

num = int(input("Digite um numero: "))
resultado = dobro(num)
print("O dobro é: ", resultado)

# Exercício 2: saudação personalizada  

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}! Você tem {idade} anos.")

# Exercício 3: Lista de frutas

frutas = ["maçã", "banana", "cereja", "abacaxi", "laranja"]
print(f"Lista de frutas: {frutas[0:3]}")

# Exercício 4: Dicionário de livro

livro = {
    "titulo": "Crime e castigo",
    "autor": "Dostoiévski",
    "ano de publicaçao": "1866"
}
print(f"Nome do autor: {livro['autor']}")

# Exercício 5: Soma dos números pares 

def soma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = soma_pares(numeros)
print("Soma dos números pares:", resultado)