#Função Dobro

def dobrar_numero(numero):
    return numero * 2

print(dobrar_numero(2))
print(dobrar_numero(5))

#Mensagem personalizada

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá {nome}! Você tem {idade} anos, seja bem vindo")

#Lista de frutas

frutas = ["maçã", "banana", "laranja", "manga", "melancia"]
print(frutas[:3])

#Dicionário livro

livro = {
    "titulo": "A Sociedade do Anel",
    "autor": "J. R. R. Tolkien",
    "ano": "1954"
}

print(livro["autor"])

#Soma dos números pares

def somar_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
        return soma
    
numeros = [2, 4, 6, 8, 10]
resultado = somar_pares(numeros)
print(resultado)