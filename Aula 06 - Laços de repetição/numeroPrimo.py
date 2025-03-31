num_inferior = 1
num_superior = 100

for num in range(3, num_superior + 1, 2):#pula de 2 em 2 porque todos os pares NÃO SÃO primos
        #ou seja, vai de 3 pra 5 pra 7 pra 9 e por ai vai
    primo = True
    for i in range(3, int(num**0.5) + 1, 2): #Checagem para saber se o número é primo ou não
        #Toda raiz quadrada de um número primo da um numero NÃO exato.
        #Se dividirmos o número pela raiz dele (num ** 0.5), 
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num:3d}")