nome = input("Digite seu nome: ")
while not (idade := input("Digite sua idade: ")).isdigit():
    print("Digite um número inteiro válido.")
idade = int(idade)
print(f"Bem-vindo(a), {nome}! Você tem {idade} anos.")

