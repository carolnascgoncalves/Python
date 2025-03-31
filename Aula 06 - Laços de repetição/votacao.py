x = True

h = 0
z = 0
l = 0

print("1- HUGUINHO \n"+
"2- ZEZINHO \n"+
"3- LUIZINHO \n"+
"0- SAIR \n")
while x:
    x = int(input("Escolha uma opção: "))
    match x:
        case 1:
            h += 1
        case 2:
            z += 1
        case 3:
            l += 1


print(f"1- HIGUINHO: {h:>5} VOTOS \n"+
f"2- ZEZINHO: {z:>6} VOTOS \n"+
f"3- LUIZINHO: {l:>5} VOTOS \n")