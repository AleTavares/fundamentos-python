# Fundamentos de Python - FAAT ADS 

Este repositório contém exemplos práticos para a aula de **Fundamentos de Python** do curso de Engenharia de Software.

## Estrutura

- Exemplos de código organizados por temas:
  - Olá Mundo e entrada de dados
  - Variáveis
  - Tipos numéricos e booleanos
  - Manipulação de strings
  - Listas e dicionários
  - Funções
  - Escopo de variáveis

## Como utilizar

1. Faça o download ou clone este repositório.
2. Abra os arquivos `.py` em seu editor de código (VS Code recomendado).
3. Execute e modifique os exemplos para praticar.

---

## Conceitos Fundamentais

### Variáveis
Variáveis são espaços na memória do computador usados para armazenar dados temporariamente durante a execução do programa. Em Python, você pode criar uma variável simplesmente atribuindo um valor a um nome. O tipo da variável é definido automaticamente pelo valor atribuído. Variáveis facilitam o armazenamento, manipulação e reutilização de informações.

### Tipos Numéricos e Booleanos
Os tipos numéricos em Python incluem inteiros (números sem casas decimais) e números de ponto flutuante (números com casas decimais). Eles são usados para cálculos matemáticos e operações aritméticas. O tipo booleano representa valores lógicos: `True` (verdadeiro) ou `False` (falso). Booleans são usados principalmente em decisões e condições do programa.

### Strings
Strings são sequências de caracteres usadas para representar textos. Em Python, você pode criar uma string usando aspas simples ou duplas. Strings permitem armazenar nomes, frases, mensagens e qualquer informação textual. Existem diversos métodos para manipular strings, como juntar, dividir, substituir ou alterar letras maiúsculas/minúsculas.

### Listas e Dicionários
Listas são coleções ordenadas de elementos, que podem ser de qualquer tipo. Elas permitem armazenar vários valores em uma única variável e acessar cada elemento por sua posição (índice). Dicionários são coleções de pares chave-valor, onde cada valor é acessado por uma chave única. Listas são úteis para conjuntos de dados ordenados, enquanto dicionários são ideais para dados estruturados.

### Funções
Funções são blocos de código que executam uma tarefa específica e podem ser reutilizados várias vezes. Elas ajudam a organizar o programa, tornando o código mais limpo e fácil de manter. Uma função pode receber valores (parâmetros), executar operações e retornar resultados. Funções são fundamentais para a modularização e reutilização do código.

### Escopo
Escopo define onde uma variável pode ser acessada dentro do programa. Variáveis criadas dentro de funções têm escopo local e só existem enquanto a função está sendo executada. Variáveis criadas fora de funções têm escopo global e podem ser acessadas por todo o programa. Entender escopo é importante para evitar erros e garantir que as variáveis sejam usadas corretamente.

---

## Exercícios

**Para entregar os exercícios:**
- Faça um **fork** deste repositório para sua conta no GitHub.
- Crie um arquivo chamado `exercicios.py` com as respostas dos exercícios abaixo.
- Após resolver, faça um **pull request** para este repositório original.
- **No título do pull request, inclua seu Nome completo e seu RA.**

### Detalhes dos exercícios

1. **Função dobro**
   - Crie uma função que receba um número como argumento e retorne o dobro desse número. Teste a função com diferentes valores para garantir que está funcionando corretamente.

2. **Mensagem personalizada**
   - Solicite ao usuário que digite seu nome e sua idade. Após receber essas informações, exiba uma mensagem de boas-vindas personalizada, incluindo o nome e a idade informados.

3. **Lista de frutas**
   - Crie uma lista contendo cinco nomes de frutas diferentes. Mostre apenas as três primeiras frutas da lista, utilizando o conceito de fatiamento de listas.

4. **Dicionário livro**
   - Crie um dicionário chamado "livro" com três informações: título, autor e ano de publicação. Mostre apenas o nome do autor utilizando o acesso por chave do dicionário.

5. **Soma dos números pares**
   - Crie uma função que receba uma lista de números inteiros. A função deve somar apenas os números pares presentes na lista e retornar o resultado da soma.

---

**Bons estudos!**



1. Função dobro
def dobro(numero): return numero * 2

Testes da função dobro
print("Dobro de 5:", dobro(5)) print("Dobro de 10:", dobro(10)) print("Dobro de -3:", dobro(-3))

2. Mensagem personalizada
nome = input("Digite seu nome: ") idade = input("Digite sua idade: ") print(f"Seja bem-vindo(a), {nome}! Você tem {idade} anos.")

3. Lista de frutas
frutas = ["Maçã", "Banana", "Laranja", "Morango", "Abacaxi"] print("As três primeiras frutas da lista são:", frutas[:3])

4. Dicionário livro
livro = { "título": "1984", "autor": "George Orwell", "ano": 1949 } print("Autor do livro:", livro["autor"])

5. Soma dos números pares
def soma_pares(lista): return sum(numero for numero in lista if numero % 2 == 0)

Teste da função soma_pares
numeros = [1, 2, 3, 4, 5, 6] print("Soma dos números pares:", soma_pares(numeros))
