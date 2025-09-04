#Exercicio 1

def dobrar(numero):
    return numero * 2

print(dobrar(2))     # Deve retornar 4
print(dobrar(5))     # Deve retornar 10
print(dobrar(-3))    # Deve retornar -6
print(dobrar(0))     # Deve retornar 0
print(dobrar(3.5))   # Deve retornar 7.0

#Exercicio 2 
nome = input("Qual é o seu nome? ")  
idade = input("Qual é a sua idade? ")

print(f"Olá, {nome}! Você tem {idade} anos.")  # Mensagem personalizada

#Exercicio 3
frutas = ["maçã", "banana", "laranja", "melancia","limao"]
print(f"Lista de frutas: {frutas}")
print(f"3 primeiras frutas: {frutas[0:3]}")

#Exercicio 4 
livro = {
    "titulo": "Clean Code",
    "autor": "Robert C. Martin",
    "ano de publicaçao": 2008,
}
print(f"Nome do autor: {livro['autor']}")

#exercicio 5
def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:  # verifica se é par
            soma += num
    return soma

# Exemplo de teste
numeros = [1, 2, 3, 4, 5, 6]
print(soma_pares(numeros))
