for i in range(65, 123, 1): #Mostra da posição 65 até a 123 na tabela ASCII
    print(f"{i} - {chr(i)}")

x = int(input("Digite um número: ")) #Converte o número por string da tabela ASCII
print(f"em string: {chr(x)}") #65 = A 

y = input("Digite uma string: ") #Mostra o número de uma string na tabela ASCII
print(f"em int: {ord(y)}") #A = 65
