#TOPICOS:
# 1 - input e print
# 2 - variáveis
# 3 - formatação
# 4 - operadores
# 5 - if/else e match
# 6 - laços de repetição
# 7 - tratamento de erro
# 8 - list/tupla/dict
# 9 - json e manipulação de arquivo
# 10 - dataframe (pandas)
# 11 - funções

# ============= INPUT e PRINT =============
print("============= INPUT e PRINT =============")

# • print vem de "imprimir", ou seja MOSTRAR
print("Serve para mostrar as coisas no console ♥")

# input vem de "entrada", ou seja INSERIR os dados
nome             =      input("Qual o seu nome? ")
#variável    #atribui        #frase que aparece



# ============= VARIÁVEIS =============
# • variáveis são caixinhas de memórias que guardam diferentes tipos de valor
# diferente do java, que fazemos: int idade
# fazemos: 
print("\n\n============= VARIÁVEIS =============")

idade = int(input("Digite sua idade: "))
#variável = tipoVariavel(input(FRASE))
#• int = número inteiro

nome = input("Digite seu nome: ")
#string não precisa de nada antes, é o padrão
#• string = caracteres

temEmprego = bool(input("Você tem emprego? true/false: "))
#• bool = verdadeiro ou falso

salario = float(input("Digite o quanto você recebe R$"))
#• float é equivalente ao double do java, ou seja, tem casa decimal



# ============= FORMATAÇÃO =============
print("\n\n============= FORMATAÇÃO =============")

# 1) formatação de frases:
# em vez de escrevermos assim:
print("Seu nome é "+nome+" e você tem "+str(idade)+" anos")
# - OBS: str(idade) serve para converter de int para string, para poder printar na frase.
#poderiamos tambem transformar uma string em int e por ai vai

# tem uma forma muito mais prática:
print(f"Seu nome é {nome} e você tem {idade} anos")
#• com o 'f' antes das aspas, podemos colocar o valor das variaveis dentro das chaves


# 2) formatação de números decimais (float)
pi = 3.14159

print(f"Pi com 2 casas decimais: {pi:.2f}")
print(f"Pi com 3 casas decimais: {pi:.3f}")
print(f"Pi com todas as casas decimais: {pi}")

#, é para mostrar no padrão de valor
print(f"Você recebe {salario:,.2f}") #mostra com virgulas e pontos, com duas casas decimais


# 3) centralização
print(f"|{nome:<10}|") #10 casas para a esquerda
print(f"|{nome:^10}|") #centralizado
print(f"|{nome:>10}|") #10 casas para a direita



# ============= OPERADORES =============
# Operadores matemáticos:
    # + -> adição
    # - -> subtração
    # * -> multiplicação
    # / -> divisão
    # // -> divisão inteira (5 // 3 = 1) (pega a parte inteira)
    # % -> módulo (5 // 3 = 2) (retorna o resto da divisão)
    # ** -> Potência

# Operadores de atribuição:
    # = -> atribui (x = 5)
    # += -> soma e atribui (x += 3 -> x = (x + 3) -> x = 8)
    # -= -> subtrai e atribui (x -= 1 -> x = (x - 1) -> x = 7)
    # isso vale para todos os operadores matemáticos 

# Operadores de comparação:
    # == -> compara (x == 5 -> "x é igual a cinco?")
    # != -> diferente (x != 5 -> "x é diferente de cinco?" se sim é true, se não false)
    # > -> maior
    # < -> menor
    # >= -> maior ou igual
    # <= -> menor ou igual

# Operadores lógicos:
    # and -> 'E' (x == 5 and y == 5 -> se X for igual a cinco E y for igual a cinco)
    # or -> 'OU' (x == 5 or y == 5 -> se X ou Y for igual a cinco)
    # not -> 'NÃO' (not x == 5 -> se X não for igual a 5)


# ============= IF/ELSE e MATCH CASE =============
print("\n\n============= IF/ELSE e MATCH CASE =============")

#Dependendo de uma situação, faz algo
if(idade >= 18):
    print("Você pode votar")
elif(idade == 16 or idade == 17): #elif = ELse + IF
    print("Você pode escolher se vota ou não")
else:
    print("Você não pode votar")

#OBS: '=' ATRIBUI um valor | '==' COMPARA um valor
#        nome = "carol"    |  if(nome == "carol")


#O match case tem o mesmo objetivo, mas utilizamos ele para menu
numero1 = int(input("Digite o 1 número: "))
numero2 = int(input("Digite o 2 número: "))

opcaoMenu = int(input("1 - Somar \n" \
"2 - Subtrair \n" \
"3 - Multiplicar \n" \
"4 - Dividir \n" \
"5 - Potência\n"))

match(opcaoMenu):
    case 1:
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
    
    case 2:
        print(f"{numero1} - {numero2} = {numero1 - numero2}")

    case 3:
        print(f"{numero1} X {numero2} = {numero1 * numero2}")

    case 4:
        print(f"{numero1} / {numero2} = {numero1 / numero2}")
    
    case 5:
        print(f"{numero1} ** {numero2} = {numero1 ** numero2}")



# ============= LAÇOS DE REPETIÇÃO =============
print("\n\n============= LAÇOS DE REPETIÇÃO =============")

# 1) WHILE -> Se repete até que uma condição seja feita
x = 0
while (x < 5): #Enquanto X for menor que 5, mostre quanto ele vale e ao final adicione mais um
    print(f"X agora vale: {x}")
    x += 1


# 2) FOR -> Faz uma determinada quantidade de vezes (utilizamos quando sabemos quantas vezes vai acontecer)
qntdAlunos = int(input("Quantos alunos deseja adicionar? "))

#para | variavel i | no | alcance (começa com x, vai até y, adiciona de 1 em 1)
for        i         in    range(       0,      qntdAlunos,         1):
    nomeAluno = input(f"Digite o nome do {i + 1}º aluno: ")



# ============= TRATAMENTO DE ERROS =============
print("\n\n============= TRATAMENTO DE ERROS =============")

# É para evitar que o programa quebre
try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Digite um valor válido")

#tente:
    #linha do código

#caso x erro aconteça: 
    #outro código


#Quando fizer um programa, teste tudo de errado que possa acontecer no console.
#Aparece no próprio console o tipo de erro e então você só precisa copiar o nome e colocar no 'except'



# ============= LIST | TUPLA | DICT =============
print("\n\n============= LIST | TUPLA | DICT =============")

# 1) LISTA
# lista é uma coleção ordenada de itens, podendo misturar tipos ou ser de uma só

lista_vazia = []
numeros = [1,2,3,4,5]
palavras = ['carol','perfeita','♥']
mista = [1, 'python', 3.14, [1,2]]

#os indices são as posições dos itens da lista
#indices começam em 0
          #0  #1  #2  #3  #4
numeros = [1,  4,  3,  8,  5]

primeiroElemento = numeros[2] # -> retorna 3

# principais MÉTODOS:
#append(item) -> adiciona algo a lista
numeros.append(7)

#remove(item) -> remove a primeira ocorrencia do item (se tiver dois números iguais, apaga o primeiro que aparecer)
numeros.remove(3)

#sort() -> ordena a lista
numeros.sort()

#index(valor) -> indica o index do valor 
print(f"index do número 4: {numeros.index(4)}")


for numero in numeros: #para cada numero na lista numeros
    print(numero)



# 2) Tupla
#Tuplas são iguais listas, porém são dados que não podem ser modificados. São uteis quando temos dados que com certeza não se alteram (que nem os estados do brasil)

tupla_vazia = () #é com parenteses em vez de colchetes



# 3) Dict 
#Dict é um dicionario que funciona em PARES 
# -> chave :  valor
#    'nome': 'carol'

pessoa = { 
    "nome": "carol",
    "idade": 18,
    "sexo": "F",
    "cidade": "São paulo"
}

# principais MÉTODOS
    #keys() -> retorna as chaves do dicionario
    #values() -> retorna os valores do dicionario
    #items() -> retorna a chave e o valor
    #get(chave, valor_default) -> retorna o valor da chave ou um valor padrão se ela não existir
    #del -> retira a chave (e o valor consequentemente)

del pessoa["cidade"]

for chave,valor in pessoa.items():
    print(f"{chave}: {valor}")


contatos = {
    "carol": "carol@gmail",
    "ana": "ana@gmail",
    "jorge": "jorge@gmail"
}

print(f"Gmail do jorge: {contatos['jorge']}")

contatos["gabi"] = "gabi@gmail" #Adicionando novo contato



# ============= JSON | MANIPULAÇÃO DE ARQUIVOS =============
print("\n\n============= JSON | MANIPULAÇÃO DE ARQUIVOS =============")
import json

contatos = {
    "carol": {
        "nome": "carolina nascimento",
        "senha": 123123,
        "telefone": "1192312311"
    }
}

#adicionando um contato a mão
contatos["erick"] = {"nome": "erick takeshi", "senha": 321321, "telefone": "1194512311"}

#JSON é utilizado para transmitir dados e armazenar dados
#utilizamos o WITH para manipular o arquivo porque ele ja fecha automaticamente após o uso

#podemos ESCREVER no arquivo, transformando em JSON
with open("arquivo.json", "w", encoding='utf-8') as arquivo: #se ele não existir, cria o arquivo
    json.dump(contatos, arquivo, indent=4)

#e podemos LER o arquivo, transformando ele em um objeto do python
with open("arquivo.json", "r") as arquivo:
    json.load(arquivo)



# ============= DATAFRAME =============
print("\n\n============= DATAFRAME =============")
import pandas as pd #escreva no terminal "pip install pandas" (caso não tenha instalado)

with open("arquivo.json", "r") as arquivo:
    dtframe = pd.read_json(arquivo)
    print(dtframe)



# ============= FUNÇÕES =============
print("\n\n============= FUNÇÕES =============")
def soma(a, b):
    return a + b

#def nomeFunção(*parametros não são necessarios"):
    #codigo

print(soma(2, 3))
