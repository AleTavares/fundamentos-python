# Funções simples

def saudar(nome):
    return f"Olá, {nome}!"

mensagem = saudar("Pedro")
print(mensagem)

def somar(a, b):
    resultado = a + b
    return resultado

total = somar(5, 3)
print(f"A soma é: {total}")