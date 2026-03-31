consumo_diario = []

print("Entrada de dados de consumo (30 dias):")

for i in range(30):
    valor = float(input(f"Digite o consumo do dia {i + 1}: "))
    consumo_diario.append(valor)

total = sum(consumo_diario)

media = total / 30

maior_valor = max(consumo_diario)
dia_maior = consumo_diario.index(maior_valor) + 1

menor_valor = min(consumo_diario)
dia_menor = consumo_diario.index(menor_valor) + 1

contador_aumento = 0
for i in range(1, len(consumo_diario)):

    if consumo_diario[i] > consumo_diario[i - 1]:
        contador_aumento = contador_aumento + 1

print("-" * 30)
print("RELATÓRIO FINAL")
print("-" * 30)
print(f"Consumo Total: {total:.2f} kWh")
print(f"Média de Consumo: {media:.2f} kWh")
print(f"O maior consumo foi {maior_valor:.2f} kWh no dia {dia_maior}")
print(f"O menor consumo foi {menor_valor:.2f} kWh no dia {dia_menor}")
print(f"O consumo subiu {contador_aumento} vezes em comparação ao dia anterior.")
