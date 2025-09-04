# Exercício 1: Função dobro
def dobro(numero):
    """Retorna o dobro de um número."""
    return numero * 2

# Testes da função dobro
print("Dobro de 4:", dobro(4))
print("Dobro de -5:", dobro(-5))
print("Dobro de 0:", dobro(0))

# Exercício 2: Mensagem personalizada
nome = input("Digite seu nome: hector")
idade = input("Digite sua idade: 22 ")
print(f"Bem-vindo, {nome}! Você tem {idade} anos.")

# Exercício 3: Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "melancia"]
print("As três primeiras frutas são:", frutas[:3])

# Exercício 4: Dicionário livro
livro = {
    "título": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano": 1954
}
print("Autor do livro:", livro["autor"])

# Exercício 5: Soma dos números pares
def soma_pares(lista):
    """Soma apenas os números pares de uma lista de inteiros."""
    return sum(num for num in lista if num % 2 == 0)

# Teste da função soma_pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print("Soma dos números pares:", soma_pares(numeros))