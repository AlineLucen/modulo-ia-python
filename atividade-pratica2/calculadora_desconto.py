nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o valor do produto: "))
porcentagem_desconto = int(input("Digite a porcentagem de desconto: "))

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"produto: {nome_produto}")
print(f"Preço do produto: {preco_original}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: {valor_desconto:.2f}")
print(f"Preço final com Desconto: {preco_final:.2f}")
