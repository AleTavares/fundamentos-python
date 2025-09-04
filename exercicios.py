 # Exercicio 1: 
def dobro(numero):
    return numero * 2

print(dobro(5))  # Saída: 10
print(dobro(10))  # Saída: 20
print(dobro(-3))  # Saída: -6
print(dobro(0))  # Saída: 0

# Exercicio 2:

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"Bem-vindo(a), {nome}! Você tem {idade} anos.")

# Exercicio 3:

frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print(frutas[:3])

# Exercicio 4:

livro = {
    "titulo": "1984",
    "autor": "George Orwell",
    "ano": 1949,
   
}
print(f"{livro['autor']}")

# Exercicio 5:
def soma_pares(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma