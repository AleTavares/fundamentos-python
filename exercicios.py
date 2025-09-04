#1. **Função dobro**
def dobro(numero):
    return numero * 2

# Teste da função dobro
# print(dobro(5))  # Exemplo de teste

#2. **Mensagem personalizada**
def mensagem_personalizada():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print(f"Bem-vindo(a), {nome}! Você tem {idade} anos.")

# mensagem_personalizada()  # Exemplo de execução

#3. **Lista de frutas**
def mostrar_frutas():
    frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
    print(frutas[:3])

# mostrar_frutas()  # Exemplo de execução

#4. **Dicionário livro**
def mostrar_autor():
    livro = {
        "título": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "ano": 1605
    }
    print(livro["autor"])

# mostrar_autor()  # Exemplo de execução

#5. **Soma dos números pares**
def soma_pares(lista):
    return sum(numero for numero in lista if numero % 2 == 0)

# Teste da função soma_pares
# print(soma_pares([1, 2, 3, 4, 5, 6]))  # Exemplo de teste