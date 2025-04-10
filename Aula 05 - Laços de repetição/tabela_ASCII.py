valor = input("valor: ")
ehnum = True

for i in valor: #Vai mostrar apenas se for número
    if(i < "0" or i > "9" and i != "."): #Tudo que vem antes de 0 na tabela ASCII são caracteres especiais e depois do 9 alfabeticos
#Ou seja, tudo que vier antes do 0 no ASCII e depois do 9 não são números
        ehnum = False
        break
    print(i)

if ehnum:
    valor = float(valor)
    print(valor, type(valor))
else:
    print("Não é um número")

#-----------------------------------------------------

valor = input("caractere pra byte: ")
print(ord(valor))

valor2 = int(input("int pra caractere: "))
print(chr(valor2))

#-----------------------------------------------------

#1- de 48 até 58 é de 0 -> 9
for i in range(48, 58, 1):
    print(chr(i))

#de 65 até 91 é de A -> Z
for i in range(65, 91, 1):
    print(chr(i))

#de 97 até 123 é de a -> z
for i in range(97, 123, 1):
    print(chr(i))
