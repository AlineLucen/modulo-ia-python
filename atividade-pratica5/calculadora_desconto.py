def calcular_desconto (preco,percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco -desconto
    return preco_final
preco_original = float(input("Digite o preço do Produto: R$ "))
desconto = float(input("Digite o percentual de desconto do Produto: "))

total = calcular_desconto(preco_original,desconto)
print(f"O preco do produto é R$ {preco_original:.2f} com o {desconto:.2f}% de desconto é : R$ {total:.2f}")