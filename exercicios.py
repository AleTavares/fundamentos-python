#Exercício 1: Função que retorna o dobro de um numero

def dobro(numero):
    return numero * 2

print(dobro(5))
print(dobro(10))
print(dobro(-2))
print(dobro(0))
print(dobro(2.5))

#Exercício 2: Mensagem Personalizada
nome = input("Digite seu nome: ")
idade = int(input("Dígite a sua idade: "))
print(f"Olá, ",nome,"! Você tem ",idade,"anos.")

#Exercício 3: Lista de Frutas
frutas = ["cereja", "kiwi", "uva", "pessêgo", "pera"]
print (frutas[0:3]) # Primeira fruta

#Exercício 4: Dicionario Livro
livro = {
    "titulo": "Percy Jackson e o Ladrão de Raios",
    "autor": "Rick Riordan",
    "ano_publicacao": 2005",
}
print(livro["autor"])

#Exercício 5: Soma dos Numeros pares
def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0;
        soma += num
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(soma_pares(lista))

