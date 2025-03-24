decimal = float(input("Digite um número decimal: "))
print(f"formatado: {decimal:.2f}")

dinheiro = float(input("Digite um valor: R$"))
print(f"R${dinheiro:,.2f}".replace(",","x").replace(".",",").replace("x","."))

inteiro = int(input("Digite um número inteiro: "))
print(f"formatado: {inteiro:05d}")

not_cientifica = float(input("Digite um número para formatação cientifica: "))
print(f"formatado: {not_cientifica:e}")

milhar = float(input("Digite um número pra separar em milhar: "))
print(f"formatado: {milhar:,}")

frase = input("Digite uma frase: ")
print(f"Frase: {frase.capitalize()}")
print(f"FRASE: {frase.upper()}")
print(f"frase: {frase.lower()}")