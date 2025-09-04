#Exercício 1: Função que retorna o dobro de um número
def dobro(numero):
    return numero * 2

print(dobro(5))
print(dobro(10))
print(dobro(-2))
print(dobro(0))
print(dobro(2.5))

#Exercício 2: Mensagem Personalizada
nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade:"))
print(f"Olá, ",nome,"! Você tem, "idade," anos.")

#Exercicio 3: Lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print (frutas[0:3])  # Primeira fruta

#Exercicio 4: Dicionario livro
livro = {
    "titulo": "O Pato Atolado",
    "autor": "Jez Alborough",
    "ano_publicacao": 1999,
}
print(livro["autor"])

#Exercicio 5: Soma dos Numeros pares
def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(soma_pares(lista))