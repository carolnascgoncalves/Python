#Tópicos: Importar bibliotecas, ordenar listas e buscar elementos
#07/08/25


#Exercicio 1
import math

numRaiz = int(input("Digite um número para obter a raiz quadrada: "))
raiz = math.sqrt(numRaiz)

print(f"A raiz quadrada de {numRaiz}, é aproximadamente: {raiz:.2f}")


#Exercicio 2
import random
numAleatorios = []

for i in range(0, 10, 1):
    numAleatorios.append(random.randint(1,100))

numAleatorios.sort()

for i in range(0, len(numAleatorios), 1):
    print(f"{i + 1}º - {numAleatorios[i]}")


#Exercicio 3
num = [3, 1, 4, 1, 5, 9, 2, 6]
numOrdem = sorted(num)
print(numOrdem)


#Exercicio 4
listaTeste = [10, 20, 30, 40]
if(25 not in listaTeste):
    print("O número 25 não está na lista!")
else:
    print("O número 25 está na lista! :)")


#Exercicio 5
for i in range(0, len(listaTeste), 1):
    if(listaTeste[i] == 40):
        print(f"Índice: {i}")


#Exercicio 6
listaNomes = ["Rafael", "Maite", "Olivia", "Beto", "Fabio"]
listaNomes.sort()


#Exercicio 7
import pandas as pd

arquivo = [
    {'nome': 'carol', 'idade': 18},
    {'nome': 'lucas', 'idade': 25},
    {'nome': 'ana', 'idade': 15}
]

frameWork = pd.DataFrame(arquivo)

print(frameWork)


#Exercicio 8
listaNum = [5, 1, 3, 2]
listaNum.sort(reverse=True)


#Exercicio 9
if(4 in listaNum):
    print("O número 4 ESTÁ na lista :)))")
    
else:
    print("O número 4 não está na lista!")


#Exercicio 10
#sorted -> cria uma nova lista e não altera a original
#sort -> altera a lista original


#Exercicio 11
Lista1 = [7, 5, 3, 9, 14]
Lista1.append(100)


#Exercicio 12
Lista2 = [1,3,5,7]
Lista2.remove(3)
print(Lista2)


#Exercicio 13
Lista2.pop((len(Lista2) - 1))
print(Lista2)


#Exercicio 14
Lista2.insert(2, 20)
print(Lista2)


#Exercicio 15
print(sum(Lista2))


#Exercicio 16
Lista3 = [24, 8, 1]
Lista2.extend(Lista3)


#Exercicio 17
print(f"tamanho: {len(Lista2)}")
print(Lista2)


#Exercicio 18
Lista2.clear()
print(Lista2)


#Exercicio 19
Lista4 = [8, 2, 5, 1]
print(f"MAX: {max(Lista4)} | MIN: {min(Lista4)}")


#Exercicio 20
pares = list(range(2, 21, 2))
print(pares)