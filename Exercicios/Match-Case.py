# 1) Peça ao usuário para digitar uma cor do semáforo ("vermelho", "amarelo" ou
# "verde") e exiba a ação correspondente:
# - "Vermelho" → "Pare!"
# - "Amarelo" → "Atenção!"
# - "Verde" → "Siga!"
# - Qualquer outra entrada → "Cor inválida!"
cor = input("(1) Cor do semáforo: ").capitalize()

match(cor):
    case 'Vermelho':
        print("Pare!")
    
    case 'Amarelo':
        print("Atenção!")
    
    case 'Verde': 
        print("Siga!")
    
    case _:
        print("Cor inválida!")

#------------------------------------------

# 2) Peça ao usuário para digitar uma operação matemálca básica ("+", "-", "*", "/").
# Solicite dois números e realize a operação escolhida.
# Caso o usuário digite um operador inválido, exiba "Operação não reconhecida".

op_matematica = input("(2) Digite uma operador matemático: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match(op_matematica):
    case '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    
    case '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    
    case '*':
        print(f"{num1} x {num2} = {num1 * num2}")

    case '/':
        print(f"{num1} / {num2} = {num1 / num2}")
    
    case _:
        print("Operação não reconhecida")

#------------------------------------------

# 3) Solicite um nome de animal ao usuário e diga a que grupo ele pertence:
# - "cachorro", "gato", "leão" → "Mamífero"
# - "cobra", "lagarto" → "Répll"
# - "águia", "papagaio" → "Ave"
# - Qualquer outra entrada → "Desconhecido"

animal = input("(3) Digite o nome de um animal: ")

match(animal):
    case "cachorro" | "gato" | "leao":
        print("Mamifero")
    
    case "cobra" | "lagarto":
        print("Reptil")
    
    case "águia" | "papagaio":
        print("Ave")
    
    case _:
        print("Desconhecido")

#------------------------------------------

# 4) Peça ao usuário para escolher um personagem digitando um número de 1 a 3:
# - 1 → "Você escolheu o Guerreiro!"
# - 2 → "Você escolheu o Mago!"
# - 3 → "Você escolheu o Arqueiro!"
# - Qualquer outro número → "Opção inválida!"
personagem = int(input("(4) Escolha um personagem: "))

match(personagem):
    case 1:
        print("Você escolheu o guerreiro!")
    
    case 2:
        print("Você escolheu o mago!")
    
    case 3: 
        print("Você escolheu o arqueiro!")
    
    case _:
        print("Opção inválida")

#------------------------------------------

# 5) Peça ao usuário para digitar uma nota de 0 a 10 e converta essa nota em um
# conceito, seguindo a seguinte tabela.

# Nota       Conceito
# 9 ou 10        A
# 7 ou 8         B
# 5 ou 6         C
# 3 ou 4         D
# 0 ou 1 ou 2    E
nota = int(input("(5) Digite a nota: "))

match(nota):
    case 9 | 10:
        print("A")
    
    case 7 | 8:
        print("B")
    
    case 5 | 6:
        print("C")
    
    case 3 | 4:
        print("D")
    
    case 0 | 1 | 2:
        print("E")

        