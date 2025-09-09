# Conversor de moeda para Dólar e Euro
valor_real = float(input("Digite o valor em reais para conversão : "))
cotacao_dolar = 5.20        
cotacao_euro = 6.15

# Conversão

conversao_dolar = valor_real / cotacao_dolar
conversao_euro = valor_real / cotacao_euro

print(f"Saldo em Reais : R$ {valor_real}")
print(f"Valor em Dolare : $ {conversao_dolar:.2f}")
print(f"Valor em Euros :  {conversao_euro:.2f}")