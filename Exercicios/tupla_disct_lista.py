frutas = ["banana", "maca", "pera", "uva", "morango"]
for i in range(0, len(frutas), 1): #Mostra a lista acima
    print(f"{i}: {frutas[i]}")

frutas.append("manga") #Adiciona a fruta manga
frutas.remove("banana") #Remove banana

frutas[2] = "abacaxi" #Troca o 3 elemento (indice 2, porque começa a contar com 0) por abacaxi 
 
for i in range(0, len(frutas), 1): #Mostra novamente a lista
    print(f"{i}: {frutas[i]}")

#-----------------------------------------------------
print(" ")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Existem {len(numeros)} na lista")

media = 0

for i in range(0, len(numeros), 1):
    media += numeros[i]

print(f"Média: {media / len(numeros)}")

#-----------------------------------------------------
pares = []

for i in range(0, len(numeros), 1):
    if(numeros[i] % 2 == 0): #Quando resto da divisão do número por 2 for zero:
        pares.append(numeros[i]) #adicione a lista o número
        
for i in range(0, len(pares), 1):
    print(pares[i])

