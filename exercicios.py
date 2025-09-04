#Exercício 1
def dobro(n): return n * 2
print("Dobro de 5:", dobro(5))

#Exercício 2
nome = input("Nome: ")
idade = input("Idade: ")
print(f"Bem-vindo(a), {nome}, {idade} anos!")

#Exercício 3
frutas = ["maçã", "banana", "laranja", "uva", "melancia"]
print("Três primeiras frutas:", frutas[:3])

#Exercício 4
livro = {"título": "O pequeno principe", "autor": " Antoine de Saint-Exupéry", "ano": 1943}
print("Autor:", livro["autor"])

#Exercício 5
def soma_pares(nums): return sum(n for n in nums if n % 2 == 0)
print("Soma dos pares:", soma_pares([1, 2, 3, 4, 5, 6]))
