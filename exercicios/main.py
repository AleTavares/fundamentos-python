def getInt(message):
    return int(input(message))

# Função para obter um valor inteiro
def getAge():
    isValid = False

    while not isValid:
        try:
            age = getInt("Qual a sua idade? ")

            isValid = True

            return age
        except Exception as e:
            print(e)
            isValid = False
            print("O valor deve ser um inteiro!")

# Função dobro
# Crie uma função que receba um número como argumento e retorne o dobro desse número. Teste a função com diferentes valores para garantir que está funcionando corretamente.
def funcaoDobro(value):
    return value * 2

# Mensagem personalizada
# Solicite ao usuário que digite seu nome e sua idade. Após receber essas informações, exiba uma mensagem de boas-vindas personalizada, incluindo o nome e a idade informados.
def nomeIdade():
    name = str(input("Qual o seu nome? "))
    age = getAge()

    print(f'Olá, { name }. Vejo que você tem { age } anos. Seja bem vindo!')

# Lista de frutas
# Crie uma lista contendo cinco nomes de frutas diferentes. Mostre apenas as três primeiras frutas da lista, utilizando o conceito de fatiamento de listas.
def listaFrutas():
    frutList = ["Maça", "Banana", "Abacaxi", "Uva", "Melancia"]

    print(frutList[:3])

# Dicionário livro
# Crie um dicionário chamado "livro" com três informações: título, autor e ano de publicação. Mostre apenas o nome do autor utilizando o acesso por chave do dicionário.
def dicionario():
    livro = {
        "titulo": "Arsène Lupin: O Ladrão de Casaca",
        "author": "Maurice Leblanc",
        "ano": "2021"
    }

    print(f"Author: { livro["author"] }")

# Soma dos números pares
# Crie uma função que receba uma lista de números inteiros. A função deve somar apenas os números pares presentes na lista e retornar o resultado da soma.
def numerosPares(numbersList):
    som = 0
    for i in numbersList:
        if (i % 2 == 0):
           som += i
    
    return som


print("\n1. Função dobro")
value = 2
dobro = funcaoDobro(value)
print(f'O dobro de { value } é { dobro }')

print("\n2. Mensagem personalizada")
nomeIdade()

print("\n3. Lista de frutas")
listaFrutas()

print("\n4. Dicionário livro")
dicionario()

print("\n5. Soma dos números pares")
som = numerosPares([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(som)