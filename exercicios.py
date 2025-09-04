def dobro(x):
    return 2 * x
print(dobro(10)) # Exercicio 1

nome = "Claudio"
idade = 31

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Boas vindas, {nome}. Sua idade é: {idade} anos.") # Exercicio 2"


frutas = ["maçã", "banana", "laranja", "uva", "melancia"]  # Exercicio 3
print(frutas[:3])


livro = {
    "titulo": "Turma da Mônica",
    "autor": "Mauricio de Sousa",
    "ano": 1970
}  
print(livro["autor"])  # Exercicio 4

def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero 
    return soma 

print(soma_pares([1, 2, 3, 4, 5, 6])) # Exercicio 5

