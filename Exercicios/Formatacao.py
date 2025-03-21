#1) Peça ao usuário um número decimal e exiba-o formatado com duas casas decimais.
numero = float(input("(1) Digite um número: "))
print(f"Formatado: {numero:.2f}")

#------------------------------------------

#2) Peça ao usuário um valor e exiba-o formatado como moeda brasileira (R$)
#Entrada: 1500.5 → Saída: R$ 1.500,50
dinheiro = float(input("(2) R$"))
print(f"Formatado: R${dinheiro:,.2f}".replace(",","x").replace(".",",").replace("x","."))

#------------------------------------------

#3) Solicite um número inteiro ao usuário e exiba-o sempre com 5 dígitos, preenchendo
#com zeros à esquerda.
num_int = int(input("(3) Digite um número inteiro: "))
print(f"Formatado: {num_int:05d}")

#------------------------------------------

#4) Peça um número ao usuário e exiba-o formatado em notação cientifica
not_cientifica = float(input("(4) Digite um número: "))
print(f"Formatação: {not_cientifica:e}")

#------------------------------------------

#5) Exibir um número com separadores de milhar
milhar = float(input("(5) Digite um número: "))
print(f"Formatação: {milhar:,}")

#------------------------------------------

#6) Converter uma string para maiúsculas, minúsculas e capitalizada
# Peça ao usuário para digitar um texto e exiba:
# • Tudo em maiúsculas
# • Tudo em minúsculas
# • Somente a primeira letra em maiúscula
texto = input("(6) Digite o texto: ")
print(f"FRASE: {texto.upper()}")
print(f"frase: {texto.lower()}")
print(f"Frase: {texto.capitalize()}")