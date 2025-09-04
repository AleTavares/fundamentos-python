#1.Função dobro

def dobro(num):
    return num * 2

print(dobro(5))  # Saída: 10
print(dobro(-3)) # Saída: -6

#2.Mensagem personalizada

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.")

#3.Listas de frutas

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
print(frutas[0:3])  # Saída: ['maçã', 'banana', 'laranja']

#4.Dicionário livro

livro = {
    "título": "harry potter",
    "autor": "j.k. rowling",
    "ano": 1997}

print(livro["autor"].title())   # Saída:Nome da autora: J.K. Rowling

#5.soma de números pares

def soma_pares(numeros):
    return sum(num for num in numeros if num % 2 == 0)

numeros = [1, 2, 3, 4, 5, 6]
print(soma_pares(numeros))  # Saída: 12 (2 + 4 + 6)