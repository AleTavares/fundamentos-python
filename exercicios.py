#exercios_py

#exercício 1
def dobro (n):
    print (f"dobro de {n} é ", 2*n)
    return 2*n 
dobro(5)

#exercício 2
def mensagem_personalizada():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print(f"Bem-vindo(a), {nome}! Você tem {idade} anos.")


# exercício 3
def lista_frutas():
    frutas = ["maçã", "banana", "laranja", "uva", "manga"]
    print("As três primeiras frutas são:", frutas[:3])

lista_frutas()


# exercício 4
def dicionario_livro():
    livro = {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899
    }
    print("Autor do livro:", livro["autor"])

dicionario_livro()


# exercício 5
def soma_pares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma

print("Exercício 5 → Soma dos pares [1,2,3,4,5,6]:", soma_pares([1, 2, 3, 4, 5, 6]))
