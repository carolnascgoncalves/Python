#1) Peça ao usuário para digitar uma nota de 0 a 10 e classifique-a da seguinte forma:
#- Nota ≥ 9 → "Excelente"
#- Nota ≥ 7 → "Bom"
#- Nota ≥ 5 → "Regular"
#- Nota < 5 → "Reprovado"

Ex1_nota = float(input("(1) Digite a nota: "))
if(Ex1_nota >= 9): print("Excelente")
elif(Ex1_nota >= 7): print("Bom")
elif(Ex1_nota >= 5): print("Regular")
else: print("Reprovado") 

#------------------------------------------

#2) Solicite um número inteiro ao usuário e diga se ele é par ou ímpar
Ex2_NumInt = int(input("(2) Digite um número: "))
if(Ex2_NumInt % 2 == 0): print("Par") #Se dividir o número por 2 e o resto da div. for 0, é par
else: print("Impar")

#------------------------------------------

#3) Cálculo de IMC - Peça ao usuário para informar peso (kg) e altura (m), calcule o IMC
#e classifique:
Ex3_Peso = float(input("(3) Digite seu peso: "))
Ex3_Altura = float(input("Digite a altura: "))
Ex3_IMC = Ex3_Peso / (Ex3_Altura ** 2)

if(Ex3_IMC >= 30): print("Obesidade")
elif(Ex3_IMC >= 25 and Ex3_IMC <= 29.9): print("Sobrepeso")
elif(Ex3_IMC >= 18.5 and Ex3_IMC <= 24.9): print("Peso normal")
else: print("Abaixo do peso")

#------------------------------------------

#4) Peça três números ao usuário e mostre qual deles é o maior.
Ex4_x = float(input("(4) Digite o 1 número: "))
Ex4_y = float(input("Digite o 2 número: "))
Ex4_z = float(input("Digite o 3 número: "))

if(Ex4_x > Ex4_y and Ex4_x > Ex4_z): print(f"{Ex4_x} é maior que {Ex4_y} e {Ex4_z}")
if(Ex4_y > Ex4_x and Ex4_y > Ex4_z): print(f"{Ex4_y} é maior que {Ex4_x} e {Ex4_z}")
if(Ex4_z > Ex4_x and Ex4_z > Ex4_y): print(f"{Ex4_z} é maior que {Ex4_x} e {Ex4_y}")

#------------------------------------------

# 5) Solicite as notas de três provas e calcule a média do aluno.
# Se a média for maior ou igual a 6, o aluno está aprovado, caso contrário, reprovado.
Ex5_n1 = float(input("(5) Primeira nota: "))
Ex5_n2 = float(input("Segunda nota: "))
Ex5_n3 = float(input("Terceira nota: "))

if(((Ex5_n1 + Ex5_n2 + Ex5_n3) / 3) >= 6): print("Aprovado") 
else: print("Reprovado")
