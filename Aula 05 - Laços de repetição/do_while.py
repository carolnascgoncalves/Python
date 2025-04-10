valor = input("valor: ")
ehnum = True

for i in valor: #Vai mostrar apenas se for número
    if(i < "0" or i > "9" and i != "."):
        ehnum = False
        break
    
    print(i)


if ehnum:
    valor = float(valor)
    print(valor, type(valor))
else:
    print("Não é um número")