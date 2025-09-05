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

frutas = ["abacate", "amora", "manga", "uva", "goiaba"]

print (frutas[0:3])



#Dicionário livro

livro = {"título": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry ", "ano": 1943}

print(livro["autor"])



#Soma dos números pares

lista = [55, 44, 33, 22, 11, 6]

def somar(lista):
    soma = 0
    for numeros in lista:
        if numeros % 2 == 0:
            soma += numeros
    return soma

print ("Os pares somados são iguais a:", somar(lista))