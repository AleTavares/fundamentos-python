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
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [10, 15, 20, 25, 30]
lista3 = [1, 3, 5, 7]

print(soma_pares(lista1))  # Esperado: 12 (2+4+6)
print(soma_pares(lista2))  # Esperado: 60 (10+20+30)
print(soma_pares(lista3))  # Esperado: 0 (nenhum par)