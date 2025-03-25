#Começa o programa sem erro
erro_venda = False
erro_cupom = False


valor = input("Venda......................: ") #Lendo valor da venda
if(valor.isdigit()): #Se o input do valor for um número: 
    if(float(valor) >= 1000): desconto = 0.1
    else: desconto = 0.05
else: #Se o input valor não for um número: muda o erro_venda para True (verdadeiro)
    erro_venda = True


#cupom.lower -> transforma tudo que for do input em caixa menor: S -> s
cupom = input("Tem cupom, [s]im ou [n]ão..: ")
if(cupom.lower() == 's' or cupom.lower() == 'n'): #Se a resposta do input cupom for 's' ou 'n' (unicas respostas válidas):
    if(cupom.lower() == 's'): cupom_desconto = 50
    else: cupom_desconto = 0

else: #Se o input não for 's' ou 'n', a resposta é inválida então o erro_cupom vira True
    erro_cupom = True


if(erro_venda == False and erro_cupom == False): #Se todos os erros são False, ele mostra o print certo
    print(f"Venda........: {float(valor):>8.2f} \n" +
          f"Desconto.....: {float(valor) * desconto:>8.2f} \n" +
          f"Cupom........: {cupom_desconto:>8.2f} \n" +
          f"Venda final..: {float(valor) - (float(valor) * desconto) - cupom_desconto:>8.2f} \n")

else: #Se algum dos erros foi mudado para True
    if(erro_venda == True and erro_cupom == True): print("Valor de venda e escolha de cupom inválidas")
    elif(erro_venda == True and erro_cupom == False): print("Valor de venda inválido")
    else: print("Escolha de cupom inválida")