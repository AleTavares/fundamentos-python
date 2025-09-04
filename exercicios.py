

# ____________________Função dobro_________________

# função???
numero=int(input("Digite um numero: "))

soma= numero *2
print(soma)


# essa eu sei que é função
def dobro(numero):
    return numero *2

print(dobro(10))
print(dobro(5))


#__________________________Mensagem personalizada_____________________

nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))

print(f"Olá {nome}, você tem {idade} anos.")


#__________________________Lista de frutas_____________________

frutas=["uva","manga","goiaba","abacaxi","melancia"]
print(f"Primeiras frutas: {frutas[0:4]}")


#__________________________Dicionário livro_____________________

livro= {
    "titulo": "malvado favorito",
    "autor": "nao sei",
    "ano": 2010,
    "genero": "animação"
}
print(f"Livro: {livro ['autor']}")


#__________________________Soma dos números pares__________________

def soma_par(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma

print(soma_par([5, 20, 3, 4, 12, 6])) 