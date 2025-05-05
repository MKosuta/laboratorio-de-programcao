#lista de compras
compras = ['maçã', 'banana', 'whey', 'batata doce']

#entrada de item e a inserção da variavel na lista compras
item = input("Digite o nome do item para adicionar a lista de compras: ")
compras.insert(1, "item")

#exibição da lista, junto com seu terceiro item
print (f"\nA lista de compras completa é: {compras}, sendo o terceiro item: {compras[2]}\n")

#remoção do primeiro item da lista
compras.pop(0)

#remoção do quarto item, que seria o último item da lista
compras.pop(3)

#inserção do item abacate no primeiro índice da lista
compras.insert(0, "abacate")

#exibição dos itens da lista um a um
for itens in compras:
    print (itens)

#itens da lista em ordem alfabética
compras.sort()
print (f"\nLista das compras em ordem alfabética: {compras}")


