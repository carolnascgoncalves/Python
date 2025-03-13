a = input("Digite sua idade: ")

# isdigit é para verificar se a resposta é um número
if a.isdigit():
    a = int(a)
    print(f"Você tem {a} anos!!")
else:
    print("Digite uma opção válida")


x = 1.6666
y = 0.9999
print(f"Arredondando: x = {round(x)} y = {round(y)}")
print(f"x - y: {round(x-y)}")