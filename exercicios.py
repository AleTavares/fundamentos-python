# exercicios.py
# Nome: José Henrique Teixeira Luiz
# RA: 3225002

# -------------------------------
# Exercício 1: Função dobro
def dobro(numero):
    return numero * 2

# Testes
print("Dobro de 5:", dobro(5))
print("Dobro de 10:", dobro(10))
print("Dobro de -3:", dobro(-3))


# -------------------------------
# Exercício 2: Mensagem personalizada
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Seja bem-vindo(a), {nome}! Você tem {idade} anos.")


# -------------------------------
# Exercício 3: Lista de frutas
frutas = ["Maçã", "Banana", "Uva", "Laranja", "Abacaxi"]
print("As três primeiras frutas da lista são:", frutas[:3])


# -------------------------------
# Exercício 4: Dicionário livro
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899
}
print("Autor do livro:", livro["autor"])


# -------------------------------
# Exercício 5: Soma dos números pares
def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

# Teste
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Soma dos números pares:", soma_pares(numeros))
