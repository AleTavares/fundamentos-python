# Escopo de variáveis

x_global = 10

def minha_funcao():
    x_local = 5
    print(f"Dentro da função (local): {x_local}")
    print(f"Dentro da função (global): {x_global}")

minha_funcao()
print(f"Fora da função (global): {x_global}")
# print(x_local) # Isso geraria um erro