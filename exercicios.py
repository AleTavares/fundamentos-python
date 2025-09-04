# Exercício 1

def dobro(x):
    return 2 * x
    
print(dobro(5))

# Exercício 2

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Exercício 3

frutas = ["maçã", "banana", "cereja", "laranja", "uva"]
print(f"3 Primeiras frutas: {frutas[:3]}")

# Exercício 4

livro = {
    "Título": "1984",
    "Autor": "George Orwell",
    "Ano": 1949
}

print("Nome do Autor:", livro["Autor"])

# Exercício 5

def soma_lista(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    return soma

lista = [1, 2, 3, 4, 5]
print("Soma dos números pares na lista:" , soma_lista(lista))