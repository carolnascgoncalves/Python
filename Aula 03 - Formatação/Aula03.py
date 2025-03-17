nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Seu nome é "+nome+" e tem "+idade+" anos")
print(f"Seu nome é {nome} e tem {idade} anos")
print("Seu nome é {} e tem {} anos".format(nome, idade))


#formatação em Float
preco = 3.141
print(f"Preço formatado: {preco:.2f}") #3.14
print(f"{preco:.3f}") #3.141
print(f"{preco:.4f}") #3.1410


#Centralização
nome2 = "Python"
print(f".{nome:<10}.") #Alinhado à esquerda
print(f".{nome:^10}.") #Centralizado
print(f".{nome:>10}.") #Alinhado à direita


# 1) Número inteiro com zeros à esquerda
num_int = 10
print(f"{num_int:05d}") #0010


#3) Números formatados com distância 10
numeros = [10.5,1,333,440.50] 
for num in numeros: 
    print(f"{num:>10,.1f}".replace('.',',')) 
    #Coloca os números a 10 casas na esquerda com 0 numeros decimais
    #Troca '.' por ',': 10.5 -> 10,5


#num:,.2f -> a virgula é pra formatação padrão de valor
num = 3000.98
print(f"{num:,.2f}") #3,000.98 (3 mil e 98 centavos) 

print(f"{num:,.2f}".replace(',','X').replace('.',',').replace('X','.'))
#3x000.98 -> 3x000,98 -> 3.000,98
