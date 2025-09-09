nome_produto = input("Digite o produto: ")
preco_unitario = float(input("Digite o valor unitario do produto: "))
quantidade = int(input("Digite a quantida de produtos:"))


#Calcula preço da venda
preco_total = preco_unitario * quantidade

print(f"\nProduto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Valor total:R${preco_total:.2f}")
