def dobro(numero):
    return numero * 2

# Testes
print(dobro(3))    # Saída esperada: 6
print(dobro(12))   # Saída esperada: 24
print(dobro(-6))   # Saída esperada: -12
print(dobro(4))    # Saída esperada: 8


nome = input("grazy: ")
idade = input("19: ")
print(f"Bem-vindo, {grazy}! Você tem {19} anos.")


frutas = ["maçã", "banana", "laranja", "uva", "melancia"]
print(frutas[:3])  # Mostra apenas as três primeiras frutas


livro = {
    "título": "Coraline",
    "autor": "Neil Gaiman",
    "ano": 2002
}

print(livro["autor"])  # Mostra apenas o nome do autor


def soma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)

# Teste da função
numeros = [1, 2, 3, 4, 5, 6]
print(soma_pares(numeros))  # Saída esperada: 12