#É um dicionário que funciona em pares, são mutáveis mas os valores não podem mudar o tipo de conteúdo, por exemplo:
#posso mudar o número, mas não posso adicionar um int pois ja é string
contatos = {
    "carol": "945414013",
    "ana": "274842192",
    "pedro": "246298722",
}

telefone_carol = contatos.get("carol")
print(f"Telefone carol: {telefone_carol}")

novo_contato = input("Digite o nome do novo contato: ")
numero_contato = input(f"Digite o número do contato {novo_contato}: ")
contatos[novo_contato] = numero_contato

print(contatos.items())

remover_contato = input("Digite um contato para ser removido: ")
del contatos[remover_contato]

print(contatos.items())

for i in contatos.items():
    print(i, "-", i[0], "-",i[1]) #0 = chave, 1 = valor