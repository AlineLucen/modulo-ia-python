distancia_pecorrida = int(input("Digite a distancia pecorrida por km: "))
combustivel_gasto = int(input("Digite a quantidade de combustivel gasto em litos: "))

consumo = distancia_pecorrida / combustivel_gasto


print("\nDados da Viagem :")
print(f"Distancia pecorrida: {distancia_pecorrida}Km")
print(f"Combustivel gasto : {combustivel_gasto} Litro(s)")
print(f"Consume Médio: {consumo:.2f} Km/l")