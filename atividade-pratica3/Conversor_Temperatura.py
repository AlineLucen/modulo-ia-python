temperatura = float(input("Digite a temperatura: "))
origem_unidade = input("Dgite a unidade  de origem (C,F ou K) : ").upper()
origem_destino = input("Digite a unidade  de destino (C,F ou K) : ").upper()

if origem_unidade == origem_destino:
    resultado = temperatura
elif origem_unidade == 'C':
    if origem_destino == 'F':
        resultado = (temperatura * 9/5) + 32
    else:
        resultado = temperatura + 273.15
  
elif origem_unidade == 'F':
    if origem_destino == 'C':
        resultado = (temperatura -32) * 5/9
    else:
        resultado = (temperatura -32) * 5/9 +273.15
else:
     if origem_destino == 'C':
         resultado = temperatura - 273.15
     else:
         resultado = (temperatura - 273.15) * 9/5 +32


print(f"{temperatura} {origem_unidade} é igual a {resultado:.2f} {origem_destino}")