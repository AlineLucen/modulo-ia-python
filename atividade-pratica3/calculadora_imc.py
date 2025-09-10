peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)


if imc < 18.5:
    print( f"seu IMC é : {imc:.2f} você foi classificado como : Abaixo do peso")
elif imc < 25:
    print(f"seu IMC é : {imc:.2f} você foi classificado como : Peso Normal")
elif imc < 30:
    print(f"seu IMC é : {imc:.2f} você foi classificado como : Sobrepeso")
else:
    print(f"seu IMC é : {imc:.2f} você foi classificado como : Obeso")
