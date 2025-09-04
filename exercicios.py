##ex1
def dobro(numero):
    return numero * 2

# Testando a função com diferentes valores
print(dobro(2))     # Saída: 4
print(dobro(5.5))   # Saída: 11.0
print(dobro(-3))    # Saída: -6
print(dobro(0))     # Saída: 0

##ex2   
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"Seja bem-vindo(a), {nome}! Você tem {idade} anos.")

##ex3
livro = {
    "título": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899
}

print("O autor do livro é:", livro["autor"])

##ex4
frutas = ["maçã", "banana", "laranja", "uva", "manga"]
print("As três primeiras frutas são:", frutas[:3])
##ex5
def soma_pares(lista):
    return sum(numero for numero in lista if numero % 2 == 0)

# Testando a função
numeros = [1, 2, 3, 4, 5, 6]
print("Soma dos números pares:", soma_pares(numeros))
