# Manipulação de strings

saudacao = "Olá"
nome = "Mundo"
mensagem = saudacao + ", " + nome + "!"
print(mensagem)

produto = "Notebook"
preco = 1500.50
print(f"O {produto} custa R${preco:.2f}.")

frase = "   Python é divertido!   "
print(f"Original: '{frase}'")
print(f"Maiúsculas: '{frase.upper()}'")
print(f"Sem espaços: '{frase.strip()}'")