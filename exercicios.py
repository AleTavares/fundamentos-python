# EXERCICIO 01: FUNCAO DOBRO
def dobro(x):
  x = int(x)
  return 2 * x

print(dobro("10"))

# EXERCICIO 02: FUNCAO SAUDACAO
def saudar():
  nome = input("Digite seu nome: ")
  idade = input("Digite sua idade: ")
  print(f"Olá {nome}, você tem {idade} anos.")
  
saudar()

# EXERCICIO 03: LISTA DE FRUTAS
frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print(frutas[:3])  # Imprime as três primeiras frutas

# EXERCICIO 04: DICIONARIO DE LIVRO
livro = {
  "titulo": "1984",
  "autor": "George Orwell",
  "ano": 1949,
}

print(livro["autor"])  # Imprime o autor do livro

# EXERCICIO 05: NUMEROS PARES
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
  if num % 2 == 0:
    pares.append(num)
soma_pares = sum(pares)
print(pares)       # Imprime a lista de números pares
print(soma_pares)  # Imprime a soma dos números pares