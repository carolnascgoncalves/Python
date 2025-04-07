alunos = []
op = True

while(op):
    print("\n1- Ver a lista \n" + 
    "2- Adicionar ou Remover aluno\n" +
    "3- Substuir aluno \n" +
    "0- Sair \n")
    op = int(input("Digite uma opção: "))

    match (op):
        case 1:
            for i in range(0, len(alunos), 1): #Pra mostar a lista
                print(f"{i + 1}: {alunos[i]}") 
        
        case 2:
            Ad_Rem = input("Deseja [a]dicionar ou [r]emover? ")
            if(Ad_Rem == "a"):
                qntd_add_aluno = int(input("Digite a quantidade de alunos para adicionar: "))
                for i in range(0, qntd_add_aluno, 1): 
                    nome_aluno = input("Digite o nome do aluno: ")
            
                    alunos.append(nome_aluno) #Pra adicionar aluno
                    print(f"Aluna(o): {nome_aluno} adicionado! \n")

            elif(Ad_Rem == "r"):
                qntd_rem_aluno = int(input("Digite a quantidade de alunos para remover: "))
                for i in range(0, qntd_rem_aluno, 1):
                    nome_aluno = input("Digite o nome do aluno: ")

                    alunos.remove(nome_aluno) #Pra remover aluno
                    print(f"Aluno {nome_aluno} removido! \n")
            else:
                print("Opção inválida")

        case 3:
            subs_aluno = input("Digite o nome do aluno: ")
            ind_aluno = int(input(f"Digite a posição da lista que deseja adicionar {subs_aluno}: "))

            alunos[ind_aluno] = subs_aluno #No índice x, colocar aluno y
        

