x = True
y = False

print(f"x e y: {x and y}") #se são iguais
print(f"x ou y: {x or y}") #se são diferentes
print(f"x e y ou x: {x and y or x}") 
print(f"x ou y ou x: {x or y or x}") 
#ORDEM DE PRIORIDADE: 1- and; 2- not; 3- or