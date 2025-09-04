def dobro(numero): # Exercício 1 - Função dobro
    return numero * 2
print(dobro(190), dobro(155))

nome = input("Digite seu nome: ") # Exercício 2 - Mensagem personalizada
idade = input("Digite sua idade: ")
print(f"Seja bem-vindo, {nome}! Você tem {idade} anos.")

frutas = ["tomate", "melancia", "manga", "limão", "morango"] # Exercício 3 - Lista de frutas
print(frutas[:3])

livro = {"título": "Percy Jackson", "autor": "Rick Riordan", "ano": 2005} # Exercício 4 - Dicionário livro
print(livro["autor"])

def soma_pares(lista): # Exercício 5 - Soma dos números pares
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

print(soma_pares([1,12,3,14,5,16]))
