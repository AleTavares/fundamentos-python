# Exercicio 4

 #4- Dicionário livro

    #Crie um dicionário chamado "livro" com três informações: título, autor e ano de publicação. 
        #Mostre apenas o nome do autor utilizando o acesso por chave do dicionário.

#dicionário livro
##livro variável que armazena o dicionário
###as chaves são "título", "autor" e "ano de publicação"
livro = {
    "título": "Aprendendo Python",
    "autor": "Saulo",
    "ano de publicação": 2025
};

#exibe o nome do autor
print("O autor do livro é:", livro["autor"]);