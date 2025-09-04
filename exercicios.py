# exercicio 1 
def dobro (n):
    return n * 4

print(dobro(2))

def dobro (n):
    return n * 8
print(dobro(2))

# exercicio 2


nome = input("Qual é o seu nome? ")  
idade = input("Qual é a sua idade? ")  
print(f"Olá, {nome}! Bem-vindo ao mundo Python.")  

# exercicio 3

frutas = ["maçã", "banana", "cereja"," laranja", "uva"]
print(f"Lista de frutas: {frutas[0:3]}")  

# exercicio 4
livros = {
    "Autor": "George Orwell",
    "O Senhor dos Anéis": "J.R.R. Tolkien",
    "O Pequeno Príncipe": "Antoine de Saint-Exupéry"
}
print(f"Autor : {livros["Autor"]}")  

# exercicio 5
def soma_pares (numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma
print(soma_pares([1, 2, 3, 4, 5, 6]))  



