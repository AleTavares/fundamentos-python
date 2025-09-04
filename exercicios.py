def dobro(numero):
    return numero * 2

# Testes
print(dobro(2))    # Saída esperada: 4
print(dobro(7))    # Saída esperada: 14
print(dobro(-3))   # Saída esperada: -6
print(dobro(0))

#  EX2
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Bem-vindo, {nome}! Você tem {idade} anos.")

# EX3
frutas = ["maçã", "banana", "laranja", "uva", "manga"]
print("As cinco primeiras frutas da lista são:")
for i in range(5):
    print(frutas[i])

# EX4
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899
}


print(livro["autor"])  # Machado de Assis
 # EX5
 
def soma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)

#
print(soma_pares([1, 2, 3, 4, 5, 6]))  # Saída esperada: 12

