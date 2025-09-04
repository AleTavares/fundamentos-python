# EXERCÍCIO 1 - Função Dobro

num = input("Digite um número para multiplicar: ")

def dobro(num):
  resultado = num * 2
  return resultado

print(f"O dobro de ", num, " é ", dobro(int(num)))


# EXERCÍCIO 2 - Mensagem Personalizada

nome = input ("Digite seu nome: ")
idade = input ("digite sua idade:")

print(f"Olá, {nome}! Você tem {idade} anos.")


# EXERCÍCIO 3 - Lista de frutas

frutas = ["morango", "pêssego", "amora", "mexerica", "romã"]

print(frutas[0:3])


# EXERCÍCIO 4 - Dicionário livro
livro = {
  "Título" : "A metamorfose",
  "Autor" : "Franz Kafka",
  "Ano" : 1915,
}

print(livro["Autor"])


# EXERCÍCIO 5 - Soma dos números pares
lista_num = [1,2,3,4,5,6]

def soma_pares(lista_num):
  soma = 0
  for num in lista_num:
    if num % 2 == 0:
      soma += num
  return soma

print(f"A soma dos números pares da lista é: {soma_pares(lista_num)}")