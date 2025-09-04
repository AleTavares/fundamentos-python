#Função dobro:

valor = int (input ("insira o valor que ira dobrar: "))

def dobrar (valor):

    resultado = valor * 2
    return (f"o número dobrado é igual a: {resultado}")
print (dobrar(valor))



#Mensagem personalizada:

nome = (input ("informe o seu nome: "))
idade = (input ("informe a sua idade: "))

print (f"Saudações {nome} , Você tem {idade} anos !")



#Lista de frutas

frutas = ["maça", "banana", "pera", "morango", "uva"]

print (frutas[0:3])



#Dicionário livro

livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}

print(livro["autor"])



#Soma dos números pares

lista = [1, 2, 3, 4, 5, 6]

def somar(lista):
    soma = 0
    for numeros in lista:
        if numeros % 2 == 0:
            soma += numeros
    return soma

print ("Os pares somados são iguais a:", somar(lista))