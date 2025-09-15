def calcular_gorjeta(valor_conta,porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

total_da_conta = 100
porcentagem = 10
gorjeta = calcular_gorjeta(total_da_conta,porcentagem)

print(f"Para uma compra de R$ {total_da_conta}, você deseja pagar {porcentagem}% de gorjeta = R${gorjeta:.2f}")