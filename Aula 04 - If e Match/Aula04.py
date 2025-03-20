x = input("Digite um número: ")

if int(x) == 0: #Transforma o x em INT para poder comparar com 0
    print(f"{x} é 0")

elif x.isdigit(): #Se x for um número (função isdigit é so pra string):
    #Transforma o x em INT, divide por 2 e compara o resto da divisão com 0
    if int(x) % 2 == 0: 
        print(f"{x} é PAR") #Se o resto da divisão for 0, então é par
    else:
        print(f"{x} é IMPAR") #Se o resto da divisão não for 0, então é ímpar

else: #Se o x não for um número:
    print("Número inválido") 

#==================================

y = float(input("Primeiro número: "))
z = float(input("Segundo número: "))

print("1- Soma \n"
"2- Subtração \n"
"3- Divisão \n"
"4- Potência \n"
"5- 'teste' \n")

escolha = int(input("Escolha uma opção: "))
match escolha: #match é como se fosse um "menu" com escolhas que podemos fazer
    case 1:
        print(f"{y} + {z} = {y+z}")
    case 2:
        print(f"{y} - {z} = {y-z}")
    case 3:
        print(f"{y} / {z} = {y/z}")
    case 4:
        print(f"{y}^{z} = {y**z}")
    case 'teste':
        print("Com string também funciona!!")

        