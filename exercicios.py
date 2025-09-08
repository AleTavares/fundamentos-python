#exercicio 1
def dobro(numero):
    return numero * 2 

print(dobro(2))
print(dobro(5))
print(dobro(10))
print(dobro(-3))

#exercicio 2

nome = imput("digite seu nome ") idade = imput("digite sua idade")
print ("ola meu nome é {nome} tem {idade} anos ")

#exercicio 3

frutas = ["banana" ,"pera" ,"abacati" ,"abacaxi" ,"mamao"]
print (frutas[0:3])

#exercicio 4 

livro = {"titulo" : "parcy jackson" 
            "anos" :"1998"
                "autor" : "cleitonaldo"}
                print (livro["autor"].title()) 

#exercicio 5

def somapares(num):
    return soma (num1 for num1 in num if num % 2 == 0)

    num = [1,2,3,4,5,6]
    print (somapares(num))
